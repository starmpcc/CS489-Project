import csv
from spider import PLAY_DOMAIN
import os
import time

def init_csv(app):
    app.reviewfile = open(app.name+'_review.tsv','w+')
    app.reviewwr = csv.writer(app.reviewfile, delimiter = '\t')


    app.metafile = open(app.name+'_meta.tsv', 'w+')
    app.metawr = csv.writer(app.reviewfile, delimiter = '\t')

    app.metawr.writerow(['Name', app.name])
    app.metawr.writerow(['Address', PLAY_DOMAIN+app.addr])
    app.metawr.writerow(['Time', 'Mean Rate', 'Total Rates', 'Rate 5', 'Rate 4', 'Rate 3', 'Rate 2', 'Rate 1'])


def write_metadata(app, t):
    t = time.gmtime(t)
    template = '{year}.{mon}.{day} {hour}:{min}'
    template = template.format(year = t.tm_year, mon = t.tm_mon, day = t.tm_mday, hour = t.tm_hour, min = t.tm_min)
    app.metawr.writerow([template, app.mean_rate, app.tot_rates, app.rate_5, app.rate_4, app.rate_3, app.rate_2, app.rate_1])


def write_all_reviews(app):
    app.reviewwr.writerow(['Writer', 'Rate', 'Date', 'Contents'])
    for i in reversed(range(len(app.writer))):
        app.reviewwr.writerow([app.writer[i], app.rate[i], app.date[i], app.contents[i]])
    

def write_new_review(app, writer, rate, date, contents):
    app.reviewwr.writerow([writer, rate, date, contents])