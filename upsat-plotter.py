#!/usr/bin/python
# Simple matplotlib script to visualize UPSat EX_WOD and WOD values
# Licenced under GPL v3
# Copyright 2016 Papamathaiou Manthos, Papadeas Pierros

# Expecting .json files in EXT_WOD_RX or WOD_RX folder

import json
from os import path
import glob
from datetime import datetime as datelib
import numpy as np
import re
import matplotlib.pyplot as plt
import sys
import getopt
import csv


argv = sys.argv[1:]
type = ''
try:
    opts, args = getopt.getopt(argv, "ht:")
except getopt.GetoptError:
    print 'upsat-plotter.py -t <EXT_WOD>/<WOD> <parameters>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'upsat-plotter.py -t [EXT_WOD/WOD] <parameters>'
        sys.exit()
    elif opt in ("-t"):
        type = arg
arg_in = sys.argv[3:]

# If EX_WOD different from WOD
if type == "EXT_WOD":
    dir_path = path.relpath("EXT_WOD_RX")
    file_list = glob.glob(dir_path + "/*.json")
    file_list.sort()

    # Initilizing values
    subsystem_key = {}
    value_key = {}
    date_list = []

    # First loop for dates
    for x in file_list:
        with open(x) as data_file:
            data = json.load(data_file)
            date_str = re.search('\d*-\d*', x).group()
            date_curent = datelib.strptime(date_str, "%Y%m%d-%H%M%S")
            date_list.append(date_curent)

    # myfile = open('export.csv', 'wb')
    # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    # wr.writerow(date_list)

    # Second loop for values
    for i in range(0, len(arg_in) / 2):
        arg_pointer = i * 2
        value_list = []

        subsystem_key[i] = arg_in[arg_pointer]
        value_key[i] = arg_in[arg_pointer + 1]

        for x in file_list:
            with open(x) as data_file:
                data = json.load(data_file)
                value = data[0]["content"][0][
                    subsystem_key[i]][0][value_key[i]]
                value_list.append(value)

        label_for_group = str(subsystem_key[i]) + "-" + str(value_key[i])

        plt.plot(np.asarray(date_list),          # X Axis
                 np.asarray(value_list),         # Y Axis
                 'o', label=label_for_group,     # Formatting
                 picker=5)                       # Picker settings

        # wr.writerow(value_list)

elif type == "WOD":
    dir_path = path.relpath("WOD_RX")
    file_list = glob.glob(dir_path + "/*.json")
    file_list.sort()

    # Initilizing values
    subsystem_key = {}
    value_key = {}
    date_list = []

    # First loop for dates
    for x in file_list:
        with open(x) as data_file:
            data = json.load(data_file)
            date_str = re.search('\d*-\d*', x).group()
            date_curent = datelib.strptime(date_str, "%Y%m%d-%H%M%S")
            date_list.append(date_curent)

    # Second loop for values
    for i in range(0, len(arg_in)):
        arg_pointer = i
        value_list = []

        value_key[i] = arg_in[arg_pointer]

        for x in file_list:
            with open(x) as data_file:
                data = json.load(data_file)
                value = data[0]["0"][0][value_key[i]]
                value_list.append(value)

        label_for_group = str(value_key[i])

        plt.plot(np.asarray(date_list),          # X Axis
                 np.asarray(value_list),         # Y Axis
                 'o', label=label_for_group,     # Formatting
                 picker=5)                       # Picker settings


else:
    print "No valid type given! Choose WOD or EXT_WOD"
    sys.exit()


plt.ylabel('Value', picker=True)
plt.xlabel('Time',  picker=True)
plt.gcf().autofmt_xdate()           # Beautify time x axis
plt.grid(True)
plt.title('UPSat Plotter')
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
plt.show()
