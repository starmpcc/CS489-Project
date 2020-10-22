from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from write_csv import *

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
        self.file = init_csv(self)

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

    write_metadata(app)


"""
void get_review(App app)
For each application, scrape the reviews in the pages.
It scrape writer's nickname, rate, written date, and the contents of the review  
The variable NUM_SCROLL define the number of pages to read
The variable SAVED_REVIEWS define the number of saved reviews in memory
"""
NUM_SCROLL = 100
SAVED_REVIEWS = 10

def get_all_reviews(app):
    driver = webdriver.PhantomJS()
    driver.get(PLAY_DOMAIN + app.addr + REVIEW_SUFFIX)
    for i in range(NUM_SCROLL):
        body = driver.find_element_by_css_selector('body')
        body.send_keys(Keys.PAGE_DOWN)

    # Reload Page with Newest Order
    driver.find_element_by_css_selector('div.W4P4ne > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div > div:nth-child(2)').click()
    driver.find_element_by_css_selector('div.W4P4ne > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1)').click()
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > span')
    for i in range(len(tmp)):
        app.writer.append(tmp[i].contents[0])

    tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.nt2C1d > div > div')
    regex = re.compile('\d')
    for i in range(len(tmp)):
        app.rate.append(regex.findall(tmp[i].get('aria-label'))[0])

    tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.p2TkOb')
    for i in range(len(tmp)):
        app.date.append(tmp[i].contents[0])

    tmp = soup.select('div > div.d15Mdf.bAhLNe > div.UD7Dzf > span:nth-child(1)')
    tmp_long = soup.select('div > div.d15Mdf.bAhLNe > div.UD7Dzf > span:nth-child(2)')

    for i in range(len(tmp)):
        if (tmp_long[i].contents):
            app.contents.append(tmp_long[i].contents[0])
        else:
            app.contents.append(tmp[i].contents[0])

    write_all_reviews(app)

    app.writer = app.writer[:SAVED_REVIEWS]
    app.rate = app.rate[:SAVED_REVIEWS]
    app.date = app.date[:SAVED_REVIEWS]
    app.contents = app.contets[:SAVED_REVIEWS]


def get_new_reviews(app):
    driver = webdriver.PhantomJS()
    driver.get(PLAY_DOMAIN + app.addr + REVIEW_SUFFIX)

    # Reload Page with Newest Order
    driver.find_element_by_css_selector('div.W4P4ne > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div > div:nth-child(2)').click()
    driver.find_element_by_css_selector('div.W4P4ne > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1)').click()
    time.sleep(3)

    for i in range(SAVED_REVIEWS):
        writer = []
        rate = []
        date = []
        contents = []
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > span')
        for j in range(len(tmp)):
            writer.append(tmp[j].contents[0])

        tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.nt2C1d > div > div')
        regex = re.compile('\d')
        for j in range(len(tmp)):
            rate.append(regex.findall(tmp[j].get('aria-label'))[0])

        tmp = soup.select('div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.p2TkOb')
        for j in range(len(tmp)):
            date.append(tmp[j].contents[0])

        tmp = soup.select('div > div.d15Mdf.bAhLNe > div.UD7Dzf > span:nth-child(1)')
        tmp_long = soup.select('div > div.d15Mdf.bAhLNe > div.UD7Dzf > span:nth-child(2)')

        for j in range(len(tmp)):
            if (tmp_long[j].contents):
                contents.append(tmp_long[j].contents[0])
            else:
                contents.append(tmp[j].contents[0])



        if (app.contents[i] in contents):
            idx = contents.index(app.contents[i])
            for j in reversed(range(idx)):
                write_new_reveiw(app, writer[j], rate[j], date[j], contents[j])
            app.writer = writer[:SAVED_REVIEWS]
            app.rate = rate[:SAVED_REVIEWS]
            app.date = date[:SAVED_REVIEWS]
            app.contents = contents[:SAVED_REVIEWS]
            break
        else:
            for j in range(10):
                body = driver.find_element_by_css_selector('body')
                body.send_keys(Keys.PAGE_DOWN)
        
        if (i == SAVED_REVIEWS -1):
            printf("ERROR-TOO MANY REVIEWS ARE DELETED")
            exit(-1)
            


if __name__ == "__main__":
    '''
    get_app_list()
    for app in app_list:
        get_metadata(app)
        get_review(app)
    '''
    app_list.append(App("Zoom","/store/apps/details?id=us.zoom.videomeetings"))
    get_metadata(app_list[0])
    get_all_reviews(app_list[0])
    while (True):
        get_new_reviews(app_list[0])