#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import numpy as np

import warnings
warnings.filterwarnings('ignore')

import_file_hgg_Dframe  = 'Truth_Jet_Detector_Reference_Frame_Data/hgg_truth_jet_information_4_bhad.csv'
import_file_hbb_Dframe  = 'Truth_Jet_Detector_Reference_Frame_Data/hbb_truth_jet_information_4_bhad.csv'
import_file_hgg_Hframe = 'Truth_Jet_Higgs_Reference_Frame_Data/hgg_truth_jet_information_4_bhad_Hframe.csv'
import_file_hbb_Hframe  = 'Truth_Jet_Higgs_Reference_Frame_Data/hbb_truth_jet_information_4_bhad_Hframe.csv'
import_file_hgg_TJframe  = 'Truth_Jet_TJ_Reference_Frame_Data/hgg_truth_jet_information_4_bhad_tjframe.csv'
import_file_hbb_TJframe = 'Truth_Jet_TJ_Reference_Frame_Data/hbb_truth_jet_information_4_bhad_tjframe.csv'

import_file_lists   = [import_file_hgg_Dframe, import_file_hbb_Dframe, import_file_hgg_Hframe, import_file_hbb_Hframe, import_file_hgg_TJframe, import_file_hbb_TJframe]
number_event_splits = [193, 214, 193, 266, 284, 266]
number_angle_splits = [38, 38, 38, 38, 38, 38, 38, 38]
angle_range_weights = [1, 1, 1, 1, 1, 1, 1, 1]
angle_range_values  = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185]
angle_centers_array = [[0 for x in range(len(number_angle_splits))] for y in range(len(import_file_lists))] 
angle_entries_array = [[0 for x in range(len(number_angle_splits))] for y in range(len(import_file_lists))]
angle_errors_array  = [[0 for x in range(len(number_angle_splits))] for y in range(len(import_file_lists))]


def angle_sort(angle_separation_deg):
    angles = np.asarray(angle_separation_deg)
    
    for i in range(len(angle_separation_deg)):
        angles[i:i+5].sort()
    
    return angles

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

#plotting angle distribution section

colors  = ['blue','orange','red','green','yellow','purple']
xlims   = [90, 180, 180]
legends = [('H->gg->bbbb Df','H->bbg->bbbb Df'), ('H->gg->bbbb Hf','H->bbg->bbbb Hf'), ('H->gg->bbbb TJf','H->bbg->bbbb TJf')]
titles  = ['Adjusted Frequency of Angle of Separation between any 2-bhad in an Event','Adjusted Frequency of Minimum Angle of Separation per Event',
           'Adjusted Frequency of Second Minumum Angle of Separation per Event', 'Adjusted Frequency of Maximum Angle of Separation per Event',
           'Adjusted Frequency of Second Maximum Angle of Separation per Event', 'Adjusted Frequency of Range (Max-Min) of Angle of Separation per Event',
           'Adjusted Frequency of Second Range (Second Max - Second Min) of Angle of Separation per Event', 'Adjusted Frequency of Average Angle of Separation per Event',]
rf      = ["Df","Hf","TJf"]
angle_type = ["any","min","second_min","max","second_max","range","second_range","average"]

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


# In[2]:





# In[20]:





# In[ ]:





# In[ ]:




