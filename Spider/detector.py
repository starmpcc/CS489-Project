import matplotlib
matplotlib.use('Agg')
import os
import csv
import time
import matplotlib.pyplot as plt
import datetime

app_list = []
root = os.path.dirname(os.path.abspath(__file__))


class Meta:
    def __init__(self):
        self.time = time.time()
        self.Mean = 0
        self.Total = 0
        self.Rate5 = 0
        self.Rate4 = 0
        self.Rate3 = 0
        self.Rate2 = 0
        self.Rate1 = 0
        self.Recalc = 0
class App:
    def __init__(self):
        self.name = None
        self.addr = None
        self.meta = []
        self.rapid_change = []
        self.deletion_list = []


def load_data(n):
    f = open(os.path.join(root, 'data', n), 'r', encoding='utf-8')
    lines = f.readlines()
    for i in range(2):
        lines[i] = lines[i].strip().split('\t')
    app = App()
    app.name = lines[0][1]
    app.addr = lines[1][1]
    app_list.append(app)
    for i in range(3, len(lines)):
        tmp = lines[i].strip().split('\t')
        meta = Meta()
        meta.Time = time.mktime(time.strptime(tmp[0], '%Y.%m.%d %H:%M'))
        meta.Mean = float(tmp[1])
        meta.Total = int(tmp[2].replace(',',''))
        meta.Rate5 = int(tmp[3])
        meta.Rate4 = int(tmp[4])
        meta.Rate3 = int(tmp[5])
        meta.Rate2 = int(tmp[6])
        meta.Rate1 = int(tmp[7])
        meta.Recalc = float((meta.Rate1 + meta.Rate2 * 2 + meta.Rate3 * 3 + meta.Rate4 * 4 + meta.Rate5 * 5)
                            /(meta.Rate1 + meta.Rate2 + meta.Rate3 + meta.Rate4 + meta.Rate5)) 
        app.meta.append(meta)


"""
Support function to refer 1st derivative statics of rate change
Not used in Program(Only for Dev)
"""
def calc_all_deriv():
    deriv = []
    for app in app_list:
        for i in range(1, len(app.meta)):
            if (app.meta[i].Time != app.meta[i-1].Time):
                deriv.append((app.meta[i].Recalc - app.meta[i-1].Recalc)/(app.meta[i].Time - app.meta[i-1].Time))
    deriv.sort()
    print(deriv)


def calc_all_deletion():
    deletion_list = []
    for app in app_list:
        for i in range(1, len(app.meta)):
            if (app.meta[i].Time != app.meta[i-1].Time):
                deletion_list.append((app.meta[i].Total - app.meta[i-1].Total)/(app.meta[i].Time - app.meta[i-1].Time))
    deletion_list.sort()
    print(deletion_list)


def detect_rapid_change():
    for app in app_list:
        rapid_change = []
        for i in range(1, len(app.meta)):
            if (app.meta[i].Time != app.meta[i-1].Time):
                if (abs((app.meta[i].Recalc - app.meta[i-1].Recalc)/(app.meta[i].Time - app.meta[i-1].Time)) >= 2e-5):
                    rapid_change.append(i)
        app.rapid_change = rapid_change


def detect_review_deletion():
    for app in app_list:
        deletion_list = []
        for i in range(1, len(app.meta)):
            if (app.meta[i].Time != app.meta[i-1].Time):
                if ((app.meta[i].Total - app.meta[i-1].Total)/(app.meta[i].Time - app.meta[i-1].Time) < -1e-2):
                    deletion_list.append(i)
        app.deletion_list = deletion_list


def plot_rate_bar():
    for app in app_list:
        rate5 = []
        rate4 = []
        rate3 = []
        rate2 = []
        rate1 = []
        t = []
        mean = []
        for i in app.meta:
            regularize = i.Total/(i.Rate5 + i.Rate4 + i.Rate3 + i.Rate2 + i.Rate1)
            rate5.append((i.Rate5 + i.Rate4 + i.Rate3 + i.Rate2 + i.Rate1 ) * regularize)
            rate4.append((i.Rate4 + i.Rate3 + i.Rate2 + i.Rate1) * regularize)
            rate3.append((i.Rate3 +i.Rate2 + i.Rate1) * regularize)
            rate2.append((i.Rate2 + i.Rate1) * regularize)
            rate1.append(i.Rate1 * regularize)
            t.append(str(datetime.datetime.fromtimestamp(i.Time)))
            mean.append(i.Mean)
        fig, ax = plt.subplots(figsize = (20, 10))
        ax.set_title(app.name, {'fontsize':25})
        ax.plot([], [], color = 'red', label = 'rapid change')
        ax.plot([], [], color = 'orange', label = 'rapid change + review deletion')
        ax.plot([], [], color = 'yellow', label = 'review deletion')
        ax.bar(range(len(t)), rate5, label = '5')
        ax.bar(range(len(t)), rate4, label = '4')
        ax.bar(range(len(t)), rate3, label = '3')
        ax.bar(range(len(t)), rate2, label = '2')
        ax.bar(range(len(t)), rate1, label = '1')
        ax.set_xticks(range(len(t)))
        ax.set_xticklabels(t)
        plt.legend(loc = 'upper left')

        for i, v in enumerate(t):
            ax.text(i - 0.3, rate5[i]*1.01, str(mean[i]))
        plt.gcf().autofmt_xdate()

        flag = 0
        if (app.rapid_change):
            flag = 1
            for i in app.rapid_change:
                start = i-1
                end = i
                plt.axvspan(start, end, facecolor = 'red', alpha = 0.5)            
        if (app.deletion_list):
            flag = 1
            for i in app.deletion_list:
                start = i-1
                end = i
                plt.axvspan(start, end, facecolor = 'yellow', alpha = 0.5)

        if (flag): 
            plt.savefig(os.path.join(root, app.name+'.png'))
        plt.close()

if __name__ == "__main__":
    l = os.listdir(os.path.join(root, 'data'))
    for i in l:
        if not 'meta' in i:
            continue
        else:
            load_data(i)
    detect_rapid_change()
    detect_review_deletion()
    for app in app_list:
        if (app.rapid_change):
            print('rate change occured: '+app.name)
        if (app.deletion_list):
            print('review deletion occured: '+app.name)
    plot_rate_bar()
