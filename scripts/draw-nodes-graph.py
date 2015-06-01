#!/usr/bin/env python
#
# To export from nodewatcher v2 database:
#
# mongoexport -d nodewatcher -c statistics -f timestamp,up --query '{"graph": -2}' > node-up-status.json
#
# Run this script as in the top-level directory containing 'main.tex':
#
# ./scripts/draw-nodes-graph.py < ./data/node-up-status.json

import fileinput
import json
import pandas
import datetime
import matplotlib.pyplot as plt

series = {}

for index, line in enumerate(fileinput.input()):
    datapoint = json.loads(line)
    up = datapoint['up']
    timestamp = int(datapoint['timestamp']['$date'] / 1000)

    series[datetime.datetime.fromtimestamp(timestamp)] = up
    last_value = up

series = pandas.Series(series)
series = pandas.rolling_mean(series, 1000)
series.plot(color='green')
plt.savefig('figures/wlansi-nodes-up.pdf')

