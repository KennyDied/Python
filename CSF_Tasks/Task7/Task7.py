import urllib.request
import xml.etree.cElementTree as ET
import numpy as np

import flask
from lxml import html as HTML

link = 'http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=14/04/2021'
XML_FILE = 'utils/quotation.xml'


def site_to_xml(url):
    f = open('utils/quotation.xml', 'w', encoding='utf-8')
    page = urllib.request.urlopen(url)
    page_text = page.read()
    f.write(str(page_text)[2:-1])
    f.close()


def all_valute():
    valutes = [[]]
    tree = ET.parse('utils//quotation.xml')
    root = tree.getroot()

    for item in root.iterfind('.//'):
        print("1 ITTER")
        valute = []
        if item.tag == 'Name':
            valute.append(item.text)
        if item.tag == 'Nominal':
            valute.append(item.text)
        if item.tag == 'Value':
            valute.append(item.text)
        print(valute)

    print(valutes)

site_to_xml(link)
all_valute()

# tree = ET.ElementTree(file=XML_FILE)
# root = tree.getroot()
#
# for child_of_root in root:
#     print(child_of_root.tag, child_of_root.attrib)

