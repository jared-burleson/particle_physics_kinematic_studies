# This file is for analyzing the angle of separation between b-hadrons in 4 b-hadron events. 
# This is done by plotting adjusted frequency distribution for different characteristics of angle of separation.
# The code presented below is a framework code, meaning that if you give it a certain number of files, 
# and fill in the specific parameters in the code, it will be able to generate any combination of plots.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import numpy as np

# I hate getting warning messages, ignored since they aren't errors.
import warnings
warnings.filterwarnings('ignore')

# This can be any number of import files to analyze, for my work, I used two different processes against each other in analysis.
# The code for plotting in based on the concept of only comparing two individual file information against each other.
# If there is a need to analyze more processes at once (say 3), then the code will need to be altered more than adding another file.
import_file_process1 = 'kinematic_information_process2_4_bhad.csv'
import_file_process2 = 'kinematic_information_process2_4_bhad.csv'

import_file_lists   = [import_file_process1, import_file_process2]
number_event_splits = np.zeros(len(import_file_lists))

for i in range(len(import_file_lists)):
    number_event_splits[i] = len(pd.read_csv(import_file_lists[i]))

# The length number of angle splits is how many different methods are analyzed in plots, I have chosen to look at 8 different methods, more or less can be chosen
# The physical value in each index for number_angle_splits is the number of bins that divides the angle data.
# angle_range_weights should have the same size as number_angle_splits, it is the weight to the angle_ranges for each analysis done/
number_angle_splits = [38, 38, 38, 38, 38, 38, 38, 38]
angle_range_weights = [1, 1, 1, 1, 1, 1, 1, 1]
angle_range_values  = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185]
angle_centers_array = [[0 for x in range(len(number_angle_splits))] for y in range(len(import_file_lists))] 
angle_entries_array = [[0 for x in range(len(number_angle_splits))] for y in range(len(import_file_lists))]
angle_errors_array  = [[0 for x in range(len(number_angle_splits))] for y in range(len(import_file_lists))]

# This function sorts the angles in an event to sort by smallest to largest angle.
def angle_sort(angle_separation_deg):
    angles = np.asarray(angle_separation_deg)
    
    for i in range(len(angle_separation_deg)):
        angles[i:i+5].sort()
    
    return angles

# This is now the main code, which is responsible for generating the different subsets of angle data on an event per each event to plot
# the frequencey distribution of, based on the value.
for i in range(len(import_file_lists)):
    data = pd.read_csv(import_file_lists[i])
    angle_separation_deg = []
    
    for j in range(len(data)):
        angle_separation_deg.append([data["angle_12"][j], data["angle_13"][j], data["angle_14"][j], data["angle_23"][j], data["angle_24"][j], data["angle_34"][j]])
    
    for j in range(len(number_angle_splits)):
        angle_count          = np.zeros(number_angle_splits[j])
        angle_amount_count   = np.zeros(number_angle_splits[j])
        angle_adjusted_count = np.zeros(number_angle_splits[j])
        angle_error          = np.zeros(number_angle_splits[j])
        adjustor = 0
        angle_count_adjusted = 0
        
        angles = angle_sort(angle_separation_deg)
        angle_values = []
        angle_ranges = []
        
        for k in range(len(angle_range_values)):
            angle_ranges.append(angle_range_values[k]*angle_range_weights[j])
        
        # These are the 8 different angle analyses done on the data
        if(j == 0): #all angles per event
            for k in range(len(angles)):
                for l in range(0,6):
                    angle_values.append(angles[k][l])
        elif(j == 1): #minimum angle per event
            for k in range(len(angles)):
                angle_values.append(angles[k][0])
        elif(j == 2): #second minimum angle per event
            for k in range(len(angles)):
                angle_values.append(angles[k][1])
        elif(j == 3): #maximum angle per event
            for k in range(len(angles)):
                angle_values.append(angles[k][5])
        elif(j == 4): #second maximum angle per event
            for k in range(len(angles)):
                angle_values.append(angles[k][4])
        elif(j == 5): #range (maximum - minimum) angle per event
            for k in range(len(angles)):
                angle_values.append(angles[k][5] - angles[k][0])
        elif(j == 6): #second range (second maximum - second minimum) angle per event
            for k in range(len(angles)):
                angle_values.append(angles[k][4] - angles[k][1])
        elif(j == 7): #average angle per event
            for k in range(len(angles)):
                angle_values.append((angles[k][0] + angles[k][1] + angles[k][2] + angles[k][3] + angles[k][4] + angles[k][5])/6)
        
        for k in range(len(angle_values)):
            angle_range_counter = 0
            while angle_range_counter < len(angle_ranges)-1:
                if(angle_values[k] >= angle_ranges[angle_range_counter] and angle_values[k] < angle_ranges[angle_range_counter+1]):
                    angle_count[angle_range_counter]+=1
                    angle_amount_count[angle_range_counter]+=angle_values[k]
                    adjustor+=1
                angle_range_counter+=1

        for k in range(len(angle_adjusted_count)):
            angle_adjusted_count[k] = angle_count[k]/adjustor
            angle_count_adjusted+=angle_adjusted_count[k]
    
        for k in range(len(angle_error)):
            angle_error[k] = math.sqrt(angle_adjusted_count[k]*(1-angle_adjusted_count[k])/adjustor)
            
        angle_error_array = np.asarray(angle_error)
        angle_count_adj_array = np.asarray(angle_adjusted_count)
        angle_adj_entries,angle_adj_edges = np.histogram(angle_ranges,bins=number_angle_splits[j],range=(0,number_angle_splits[j]*(5*angle_range_weights[j])),weights=angle_count_adj_array)
        angle_adj_bin_centers = 0.5*(angle_adj_edges[:-1] + angle_adj_edges[1:])
        
        angle_centers_array[i][j] = angle_adj_bin_centers
        angle_entries_array[i][j] = angle_adj_entries
        angle_errors_array[i][j]  = angle_error_array

# plotting angle distribution section

colors  = [color1, color2]
xlims   = [xlim_value]
legends = [(process1_name,process2_name)]
titles  = [] #Whatever titles you want
rf      = [] #Whatever reference frame the data is analyzed in 
angle_type = ["any","min","second_min","max","second_max","range","second_range","average"] #This is default, what I did, but can be changed

for i in range(int(len(import_file_lists)/2)):
    for j in range(len(number_angle_splits)):
        plt.bar(angle_centers_array[2*i][j], angle_entries_array[2*i][j], color=colors[2*i], width=5*angle_range_weights[j], yerr=angle_errors_array[2*i][j], ecolor='black', capsize=3, edgecolor='black', alpha=0.5)
        plt.bar(angle_centers_array[2*i+1][j], angle_entries_array[2*i+1][j], color=colors[2*i+1], width=5*angle_range_weights[j], edgecolor='black', alpha=0.5)
        ax = plt.subplot()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(15))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
        plt.xlim(0,180)
        plt.xlabel('Angle of Separation (5 Degree Intervals)')
        plt.ylabel('Adjusted Frequency (1 = 100%)')
        plt.legend(legends[i])
        plt.title(titles[j])
        plt.savefig("Angle_Plots/Hgg_Hbb_"+str(rf[i])+"_"+str(angle_type[j]),dpi=300, bbox_inches='tight')
        plt.show()
