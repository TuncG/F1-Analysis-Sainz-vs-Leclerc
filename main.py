import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np
import pandas as pd
from fastf1 import utils

#I want to analyze lap times in quali and quali positions
#get fastest times in fp1,fp2,fp3 and Q as well as placement times and compare them
#I want to analyze race finishes and who was fastest in each sector



final_data = {} # Final data will be stored in { Race: [{Driver : {'session" : LapTime}]}}
# "Brazil GP", "QATAR GRAND PRIX", "Saudi Arabia GP", "ABU DHABI GRAND PRIX"
selected_races = ["Mexico GP"]

selected_sessions = ['FP1', 'FP2']#'FP3', 'Q'
temp_var = {}

drivers = ['LEC','SAI']

k = 0

for i in selected_races:
    final_data[i] = {}
    while k < len(drivers):
        temp_driver = {drivers[k]:{}}

        for l in selected_sessions:
            temp = ff1.get_session(2021, i, l).load_laps()
            temp_time = temp.pick_driver(drivers[k]).pick_fastest()
            test = str(temp_time['LapTime'])
            final_temp = test[7:]
            last_lap_times = temp_driver.get(drivers[k])
            last_lap_times[l] =  final_temp
            temp_driver[drivers[k]] = last_lap_times

        temp_data = final_data.get(i)
        temp_driver.update(temp_data)
        final_data[i] = temp_driver

        k += 1

print(final_data)

lec_difference = []
sai_difference = []

def Compare_Times(data):

    for i in selected_races:


        pass


Compare_Times(final_data)
