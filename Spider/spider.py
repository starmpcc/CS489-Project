from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app_list = []

#Global Addresses
CHART_ADDR = "https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU"
PLAY_DOMAIN = "https://play.google.com"
REVIEW_SUFFIX = "&showAllReviews=true"

class App:
    rate_5 = 0
    rate_4 = 0
    rate_3 = 0
    rate_2 = 0
    rate_1 = 0
    tot_rates = 0
    mean_rate = 0
    writer = []
    rate = []
    date = []
    contents = []
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        req = requests.get(PLAY_DOMAIN + addr)
        self.soup = BeautifulSoup(req.text, 'html.parser')


"""
void get_app_list(void)
Get list of Apps on popular/free chart in Google Play
And scrape the app introduction main pages
Save them into list app_list
"""
def get_app_list():
    req = requests.get(CHART_ADDR)
    soup = BeautifulSoup(req.text, 'html.parser')
    names = soup.select('c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a > div')
    addrs = soup.select('c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a')
    for i in range(len(names)):
        name =  names[i].get('title')
        addr = addrs[i].get('href')
        app_list.append(App(name, addr))

"""
void get_metadata(App app)
For each application, scrape the metadata of rates.
It includes mean rate, total rates, ratio of each rates, 
"""
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



"""
void get_review(App app)
For each application, scrape the reviews in the pages.
It scrape writer's nickname, rate, written date, and the contents of the review  
The variable num_scroll define the number of pages to read
"""
num_scroll = 10

def get_review(app):
    driver = webdriver.PhantomJS()
    driver.get(PLAY_DOMAIN + app.addr + REVIEW_SUFFIX)
    for i in range(num_scroll):
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    


    tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > span')
    for i in range(len(tmp)):
        app.writer.append(tmp[i].contents[0])
    print(app.writer)

    tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.nt2C1d > div > div')
    regex = re.compile('\d')
    for i in range(len(tmp)):
        app.rate.append(regex.findall(tmp[i].get('aria-label'))[0])
    print(app.rate)

    tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.p2TkOb')
    for i in range(len(tmp)):
        app.date.append(tmp[i].contents[0])
    print(app.date)

    tmp = soup.select('div > div.d15Mdf.bAhLNe > div.UD7Dzf > span:nth-child(1)')
    tmp_long = soup.select('div > div.d15Mdf.bAhLNe > div.UD7Dzf > span:nth-child(2)')
    for i in range(len(tmp)):
        if (len(tmp_long[i].contents[0])):
            app.contents.append(tmp_long[i].contents[0])
        else:
            app.contents.append(tmp[i].contents[0])
    print(app.contents)


'''
get_app_list()
for app in app_list:
    get_metadata(app)
    get_review(app)
'''

app_list.append(App("Zoom","/store/apps/details?id=us.zoom.videomeetings"))
get_metadata(app_list[0])
get_review(app_list[0])