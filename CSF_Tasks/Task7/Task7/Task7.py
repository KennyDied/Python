import urllib.request
import xml.etree.cElementTree as ET
from flask import Flask, render_template, request

link = 'http://www.cbr.ru/scripts/XML_daily_eng.asp?date_req=02/05/2021'
XML_FILE = 'utils/quotation.xml'


def site_to_xml(url):
    f = open('utils/quotation.xml', 'w', encoding='utf-8')
    page = urllib.request.urlopen(url)
    page_text = page.read()
    f.write(str(page_text)[2:-1])
    f.close()


def all_valute():
    valutes = []
    tree = ET.parse('utils//quotation.xml')
    root = tree.getroot()
    names = []
    nominals = []
    values = []
    for item in root.iterfind('.//'):
        if item.tag == 'Name':
            names.append(item.text)
        if item.tag == 'Nominal':
            nominals.append(item.text)
        if item.tag == 'Value':
            values.append(item.text.replace(',', '.'))
    valutes.append(names)
    valutes.append(nominals)
    valutes.append(values)
    return valutes


def convert(num, ind1, ind2):
    from_valute = []
    to_valute = []
    from_valute.append(mass[0][ind1])
    from_valute.append(mass[1][ind1])
    from_valute.append(mass[2][ind1])
    to_valute.append(mass[0][ind2])
    to_valute.append(mass[1][ind2])
    to_valute.append(mass[2][ind2])

    item1 = float(from_valute[2])
    item2 = float(to_valute[2])
    return int(num) * item1/item2


site_to_xml(link)
mass = all_valute()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    res = 0
    params_post = {}
    for p in request.form:
        params_post[p] = request.form[p]
    if request.method == 'POST':
        item = tuple(params_post.items())[0][1]
        ind1 = mass[0].index(item)
        item = tuple(params_post.items())[1][1]
        ind2 = mass[0].index(item)
        num = tuple(params_post.items())[2][1]
        res = (convert(num, ind1, ind2))
    return render_template('index.html', valutes=mass[0], params_post=params_post, result=res)


if __name__ == '__main__':
    app.run()