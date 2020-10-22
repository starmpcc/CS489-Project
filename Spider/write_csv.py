import csv
from spider import *

def init_csv(app):
    app.file = open(app.name+'.csv','w+')
    wr = csv.writer(app.file)
    wr.writerow(['Name', app.name])
    wr.writerow(['Address', PLAY_DOMAIN+app.addr])
    
def write_metadata(app):
    wr = csv.writer(app.file)
    wr.writerow(['Mean Rate', app.mean_rate])
    wr.writerow(['Total Rates', app.tot_rates])
    wr.writerow(['Rate 5', app.rate_5])
    wr.writerow(['Rate 4', app.rate_4])
    wr.writerow(['Rate 3', app.rate_3])
    wr.writerow(['Rate 2', app.rate_2])
    wr.writerow(['Rate 1', app.rate_1])

def write_all_reviews(app):
    wr = csv.writer(app.file)
    wr.writerow(['Writer', 'Rate', 'Date', 'Contents'])
    for i in reversed(range(len(app.writer))):
        wr.writerow([app.writer[i], app.rate[i], app.date[i], app.contents[i]])
    
def write_new_review(app, writer, rate, date, contents):
    wr = csv.writer(app.file)
    wr.writerow([writer, rate, date, contents])