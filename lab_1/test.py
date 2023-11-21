import matplotlib.pyplot as plt
import requests
import json

json_link = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

data = json_link.json()

print(data)

dates = []

dates.append(data['Date'])

for _ in range(42):
    json_link = requests.get('https:' + data['PreviousURL'])
    data = json_link.json()
    dates.append(data['Date'])

currencies = {}

for x in data["Valute"]:
    currencies[x] = []

values = currencies

json_link = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = json_link.json()

for i in range(43):
    valute_dict = data["Valute"].items()
    for k, x in valute_dict:
        values[k].append(x["Value"])
    json_link = requests.get('https:'+data["PreviousURL"])
    data = json_link.json()

import numpy as np

fig = plt.figure()
plot = fig.add_subplot(projection="3d")

yticks = [3, 2, 1, 0]

valutes = {}
for k, x in values.items():
    if len(valutes) < 43:
        valutes[k] = x[:43]
    else:
        break
print(valutes)

keys = list(valutes.keys())
valutes = list(valutes.values())
x_dates = np.arange(43)

for i in range(43):
    plt.plot(x_dates, valutes[i], zs=i, zdir='y', color='b', alpha=0.8)

plot.set_xlabel("date")
plot.set_ylabel("valute")
plot.set_zlabel("value")

plot.set_yticks(np.arange(43),keys)

plt.show()
