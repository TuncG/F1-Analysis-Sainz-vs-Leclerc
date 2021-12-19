import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np
import pandas as pd

#I want to analyze lap times in quali and quali positions
#get fastest times in fp1,fp2,fp3 and Q as well as placement times and compare them
#I want to analyze race finishes and who was fastest in each sector



final_data = {}
# "Brazil GP", "QATAR GRAND PRIX", "Saudi Arabia GP", "ABU DHABI GRAND PRIX"
selected_races = ["Mexico GP"]

selected_sessions = ['FP1', 'FP2', 'FP3', 'Q']
temp_var = {}

drivers = ['LEC','SAI']


for i in selected_races:
    for k in drivers:
        final_data[i] = {k:[]}
        for l in selected_sessions:
            temp = ff1.get_session(2021, i, l).load_laps()
            temp_time = temp.pick_driver(k).pick_fastest()
            final_temp = {l: temp_time['LapTime']}
            last_lap_times = final_data[i].get(k)
            last_lap_times.append(final_temp)
            final_data[i][k] = last_lap_times

print(final_data["Mexico GP"])
