import matplotlib
matplotlib.use('Agg')
import os
import csv
import time
import matplotlib.pyplot as plt
app_list = []
root = os.path.dirname(os.path.abspath(__file__))


class Meta:
    def __init__(self):
        self.time = 0
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
    rapid_change = []
    for app in app_list:
        for i in range(1, len(app.meta)):
            if (app.meta[i].Time != app.meta[i-1].Time):
                if (abs((app.meta[i].Recalc - app.meta[i-1].Recalc)/(app.meta[i].Time - app.meta[i-1].Time)) >= 2e-5):
                    rapid_change.append((app.name, app.meta[i]))
    return rapid_change


def detect_review_deletion():
    deletion_list = []
    for app in app_list:
        for i in range(1, len(app.meta)):
            if (app.meta[i].Time != app.meta[i-1].Time):
                if ((app.meta[i].Total - app.meta[i-1].Total)/(app.meta[i].Time - app.meta[i-1].Time) < 1e-2):
                    deletion_list.append((app.name, app.meta[i]))
    return deletion_list

def plot_rate_bar():
    for app in app_list:
        rate5 = []
        rate4 = []
        rate3 = []
        rate2 = []
        rate1 = []
        time = []
        for i in app.meta:
            regularize = 100/(i.Rate5 + i.Rate4 + i.Rate3 + i.Rate2 + i.Rate1)
            rate5.append((i.Rate5 + i.Rate4 + i.Rate3 + i.Rate2 + i.Rate1 ) * regularize)
            rate4.append((i.Rate4 + i.Rate3 + i.Rate2 + i.Rate1) * regularize)
            rate3.append((i.Rate3 +i.Rate2 + i.Rate1) * regularize)
            rate2.append((i.Rate2 + i.Rate1) * regularize)
            rate1.append(i.Rate1 * regularize)
            time.append(i.Time)
        plt.bar(range(len(rate1)), rate5)
        plt.bar(range(len(rate1)), rate4)
        plt.bar(range(len(rate1)), rate3)
        plt.bar(range(len(rate1)), rate2)
        plt.bar(range(len(rate1)), rate1)


        plt.savefig('temp.png')
        plt.show()

        break

if __name__ == "__main__":
    l = os.listdir(os.path.join(root, 'data'))
    for i in l:
        if not 'meta' in i:
            continue
        else:
            load_data(i)

    plot_rate_bar()
