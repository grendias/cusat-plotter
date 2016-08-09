import json
from os import path
from pprint import pprint
import glob
import datetime
import re
import matplotlib.pyplot as plt
import sys
import matplotlib.dates as mdates

subsystem_key = sys.argv[1]
value_key = sys.argv[2]
dir_path = path.relpath("EXT_WOD_RX")
file_list = glob.glob(dir_path+"/*.json")
date_list = []
value_list = []

file_list.sort()

for x in file_list:
    with open(x) as data_file:
        data = json.load(data_file)
        value = data[0]["content"][0][subsystem_key][0][value_key]
        date_str = re.search('\d*-\d*', x).group()
        date_curent = datetime.datetime.strptime(date_str, "%Y%m%d-%H%M%S")
        date_list.append(date_curent)
        value_list.append(value)

#pprint( date_list)
plot_dates  = mdates.date2num(date_list)
plt.plot(date_list, value_list)
plt.show()

