from bs4 import BeautifulSoup
import requests
import re
import time
import sys
import os
import csv

app_list = []
SAVED_REVIEWS = 10

#Global Addresses
CHART_ADDR = "https://play.google.com/store/apps/collection/cluster?clp=0g4gCh4KGHRvcHNlbGxpbmdfbmV3X2ZyZWVfR0FNRRAHGAM%3D:S:ANO1ljIxjbU&gsr=CiPSDiAKHgoYdG9wc2VsbGluZ19uZXdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJL0LQ"
PLAY_DOMAIN = "https://play.google.com"
LOCALE_SUFFIX= "&hl=en_US&gl=US"
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
    wr = None
    file = None
    name = None
    addr = None
    soup = None
    metawr = None
    reviewwr = None
    reviewfile = None
    metafile = None
    def init(self, name, addr):
        self.name = name
        self.addr = addr
        req = requests.get(PLAY_DOMAIN + addr + LOCALE_SUFFIX)
        self.soup = BeautifulSoup(req.text, 'html.parser')
        init_csv(self)

"""
void get_metadata(App app)
For each application, scrape the metadata of rates.
It includes mean rate, total rates, ratio of each rates, 
"""
def get_metadata(app):
    t = time.time()
    req = requests.get(PLAY_DOMAIN + app.addr)
    app.soup = BeautifulSoup(req.text, 'html.parser')
    
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

    write_metadata(app, t)


def load_data():
    name_list = os.listdir(os.getcwd() + '\data\\')
    for n in name_list:
        if 'meta' in n:
            f = open('.\data\\'+n, 'r', encoding='utf-8')
            lines = f.readlines()
            for i in range(2):
                lines[i] = lines[i].strip().split('\t')
            app = App()
            app.name = lines[0][1]
            app.addr = lines[1][1]

            f.close()
            f = open('.\data\\'+app.name+'_review.tsv','r', encoding='utf-8')
            lines = f.readlines()
            for i in range(-1, -SAVED_REVIEWS -1, -1):
                lines[i] = lines[i].strip().split('\t')
                app.writer.append(lines[i][0])
                app.rate.append(lines[i][1])
                app.date.append(lines[i][2])
                app.contents.append(lines[i][3])
            f.close()

            app.reviewfile = open('.\data\\'+app.name+'_review.tsv','a', encoding='utf-8', newline='')
            app.reviewwr = csv.writer(app.reviewfile, delimiter = '\t')

            app.metafile = open('.\data\\'+app.name+'_meta.tsv', 'a', encoding='utf-8', newline='')
            app.metawr = csv.writer(app.metafile, delimiter = '\t')

            app_list.append(app)
        
        else:
            continue

def init_csv(app):
    app.reviewfile = open('data\\'+app.name+'_review.tsv','w+', encoding='utf-8', newline='')
    app.reviewwr = csv.writer(app.reviewfile, delimiter = '\t')

    app.metafile = open('data\\'+app.name+'_meta.tsv', 'w+', encoding='utf-8', newline='')
    app.metawr = csv.writer(app.metafile, delimiter = '\t')

    app.metawr.writerow(['Name', app.name])
    app.metawr.writerow(['Address', app.addr])
    app.metawr.writerow(['Time', 'Mean Rate', 'Total Rates', 'Rate 5', 'Rate 4', 'Rate 3', 'Rate 2', 'Rate 1'])


def write_metadata(app, t):
    t = time.gmtime(t)
    template = '{year}.{mon}.{day} {hour}:{min}'
    template = template.format(year = t.tm_year, mon = t.tm_mon, day = t.tm_mday, hour = t.tm_hour, min = t.tm_min)
    #print(template)
    app.metawr.writerow([template, app.mean_rate, app.tot_rates, app.rate_5, app.rate_4, app.rate_3, app.rate_2, app.rate_1])


if __name__ == "__main__":
    load_data()        
    cycle = 0
    while True:
        #get metadata for each hour
        for app in app_list:
            get_metadata(app)
#                get_new_reviews(app)
        cycle +=1
        print(cycle)      
        time.sleep(3600)          