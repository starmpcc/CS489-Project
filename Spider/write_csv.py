import csv
from spider import *

def init_csv(app):
    app.file = open(app.name+'.csv','w+')
    app.wr = csv.writer(app.file, delimiter = '\t')
    app.wr.writerow(['Name', app.name])
    app.wr.writerow(['Address', PLAY_DOMAIN+app.addr])
    
def write_metadata(app):
    app.wr.writerow(['Mean Rate', app.mean_rate])
    app.wr.writerow(['Total Rates', app.tot_rates])
    app.wr.writerow(['Rate 5', app.rate_5])
    app.wr.writerow(['Rate 4', app.rate_4])
    app.wr.writerow(['Rate 3', app.rate_3])
    app.wr.writerow(['Rate 2', app.rate_2])
    app.wr.writerow(['Rate 1', app.rate_1])

def write_all_reviews(app):
    app.wr.writerow(['Writer', 'Rate', 'Date', 'Contents'])
    for i in reversed(range(len(app.writer))):
        app.wr.writerow([app.writer[i], app.rate[i], app.date[i], app.contents[i]])
    
def write_new_review(app, writer, rate, date, contents):
    app.wr.writerow([writer, rate, date, contents])