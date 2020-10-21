from bs4 import BeautifulSoup
import requests
import re

app_list = []
class App:
    rate_5 = 0
    rate_4 = 0
    rate_3 = 0
    rate_2 = 0
    rate_1 = 0
    tot_rates = 0
    mean_rate = 0
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        req = requests.get(play_domain + addr)
        self.soup = BeautifulSoup(req.text, 'html.parser')
    
chart_addr = "https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU"
play_domain = "https://play.google.com"

def get_app_list():
    req = requests.get(chart_addr)
    soup = BeautifulSoup(req.text, 'html.parser')
    names = soup.select('c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div')
    addrs = soup.select('c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a')
    for i in range(len(names)):
        name =  names[i].get('title')
        addr = addrs[i].get('href')
        app_list.append(App(name, addr))


def get_metadata(app):
    tmp = app.soup.select('div.W4P4ne > c-wiz > div.K9wGie > div.BHMmbe')
    app.mean_rate = tmp[0].contents[0]

    tmp = app.soup.select('div.W4P4ne > c-wiz > div.K9wGie > span > span:nth-child(2)')
    app.tot_rates = tmp[0].contents[0]

    regex = re.compile(r'\d+')

    tmp = app.soup.select('div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(1) > span.L2o20d.P41RMc')
    tmp = tmp[0].get('style')
    app.rate_5 = regex.findall(tmp)[0]

    tmp = app.soup.select('div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(2) > span.L2o20d.tpbQF')
    print(tmp)
    tmp = tmp[0].get('style')
    app.rate_4 = regex.findall(tmp)[0]

    tmp = app.soup.select('div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(3) > span.L2o20d.Sthl9e')
    tmp = tmp[0].get('style')
    app.rate_3 = regex.findall(tmp)[0]

    tmp = app.soup.select('div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(4) > span.L2o20d.rhCabb')
    tmp = tmp[0].get('style')
    app.rate_2 = regex.findall(tmp)[0]

    tmp = app.soup.select('div.W4P4ne > c-wiz > div.VEF2C > div:nth-child(5) > span.L2o20d.A3ihhc')
    tmp = tmp[0].get('style')
    app.rate_1 = regex.findall(tmp)[0]


get_app_list()
#app_list.append(App("Zoom","/store/apps/details?id=us.zoom.videomeetings"))

for app in app_list:
    get_metadata(app)

