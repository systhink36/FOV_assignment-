import urllib.request

import pandas as pd
from bs4 import BeautifulSoup


def getHTMLcontent(link):
    page = urllib.request.urlopen(link)
    Soup = BeautifulSoup(page, 'html.parser')
    return Soup


def genrateData(url):
    site = getHTMLcontent(url)
    tables = site.find_all('table')
    for table in tables:
        A = []
        B = []
        C = []
        D = []
        E = []
        F = []
        G = []
        H = []
        I = []
        J = []
        K = []
        L = []
        M = []

        rows = table.find_all('tr')[3:]
        for tr in rows:
             data = tr.find_all('td')
             if len(data)>1:
                 A.append(data[0].get_text().strip())
                 B.append(data[1].get_text().strip())
                 C.append(data[2].get_text().strip())
                 D.append(data[3].get_text().strip())
                 E.append(data[4].get_text().strip())
                 F.append(data[5].get_text().strip())
                 G.append(data[6].get_text().strip())
                 H.append(data[7].get_text().strip())
                 I.append(data[8].get_text().strip())
                 J.append(data[9].get_text().strip())
                 K.append(data[10].get_text().strip())
                 L.append(data[11].get_text().strip())
                 M.append(data[12].get_text().strip())

        tab = {'year':A, 'January':B , 'Feb': C, 'March':D, 'April':E, 'May':F, 'June':G, 'July':H, 'August': I, 'September':J,'October':K, 'November':L, 'December':M}
        dataset = pd.DataFrame(tab)

        return dataset


data1 = genrateData('http://123.63.203.150/avgrain.htm')
data2 = genrateData('http://123.63.203.150/avgrain03.htm')


data3 = pd.concat([data1, data2], ignore_index=True)


data3.to_csv("Dataset.csv", index = False)
print(data3)










