#!/usr/bin/env python
# Simple matplotlib script to visualize UPSat EX_WOD values
# Licenced under GPL v3
# Copyright 2016 Papamathaiou Manthos, Papadeas Pierros

# Expecting .json files in EXT_WOD_RX folder

import json
from os import path
import glob
from datetime import datetime as datelib
import numpy as np
import re
import matplotlib.pyplot as plt
import sys
import matplotlib.dates as mdates

# Reading the arguments
# e.g format: OBC Time ADCS "Boot Cnt" COMMS Time
arg_in = sys.argv[1:]

# Reading files
dir_path = path.relpath("EXT_WOD_RX")
file_list = glob.glob(dir_path+"/*.json")
file_list.sort()

# Initilizing values
subsystem_key = {}
value_key = {}
main_list = []
values_to_plot = []
date_list = []
plot_list = []
fig = plt.figure()

# First loop for dates
for x in file_list:
    with open(x) as data_file:
        data = json.load(data_file)
        date_str = re.search('\d*-\d*', x).group()
        date_curent = datelib.strptime(date_str, "%Y%m%d-%H%M%S")
        date_list.append(date_curent)

# Second loop for values
for i in range(0, len(arg_in) / 2):
    arg_pointer = i * 2
    pointer = i * 3
    value_list = []

    subsystem_key[i] = arg_in[arg_pointer]
    value_key[i] = arg_in[arg_pointer + 1]

    for x in file_list:
        with open(x) as data_file:
            data = json.load(data_file)
            value = data[0]["content"][0][subsystem_key[i]][0][value_key[i]]
            value_list.append(value)

    label_for_group = str(subsystem_key[i]) + "-" + str(value_key[i])

    plt.plot(np.asarray(date_list),          # X Axis
             np.asarray(value_list),         # Y Axis
             'o', label=label_for_group,     # Formatting
             picker=5)                       # Picker settings


# On pick event
def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    # TODO: We need to print those values in the plot
    print 'Time='+str(np.take(xdata, ind)[0])  # Print X point
    print 'Value='+str(np.take(ydata, ind)[0])  # Print Y point

# Plot the values
plot_dates = mdates.date2num(date_list)
plt.ylabel('Value', picker=True)
plt.xlabel('Time',  picker=True)
plt.gcf().autofmt_xdate()           # Beautify time x axis
plt.grid(True)
plt.title('UPSat EX_WOD')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
