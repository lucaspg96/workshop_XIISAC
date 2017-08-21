import urllib.request as req
from bs4 import BeautifulSoup as bs
from pprint import pprint

def getDolar():
	url = "http://dolarhoje.com/"
	site = req.urlopen(url).read()
	html = bs(site,"html.parser")
	valor = html.find_all("input",\
		{"id":"nacional"})[0]

	return valor.get("value")

def get_menu_text(menu):
	text = ""
	for meal in menu:
		text += meal["name"] + "\n"

		for category in meal["categories"]:
			text += "- {}:\n\t".format(category["name"])

			text+=", ".join(category["options"])
			text+="\n"

		text+="\n"

	return text

def get_menu():
	url = "http://www.ufc.br/restaurante/cardapio/1-restaurante-universitario-de-fortaleza"
	site = req.urlopen(url).read()
	html = bs(site,"html.parser")

	table = html.find_all("tbody")[0]

	lines = table.find_all("tr")

	menu = []

	for line in lines:
		columns = line.find_all("td")

		if(len(columns)<=1):
			#refeição
			name = columns[0].find_all("h3")[0].get_text()
			menu.append({"name":name,"categories":[]})

		else:
			category = columns[0].find_all("span")[0].get_text()
			options = []
			for op in columns[1].find_all("span"):
				if '(' not in op.get_text():
					options.append(op.get_text())
				else:
					options[-1] = options[-1]+" {}".format(op.get_text())
			menu[-1]["categories"].append({"name":category,"options":options})

	return get_menu_text(menu)