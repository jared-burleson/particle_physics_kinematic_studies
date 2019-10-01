#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import numpy as np
from itertools import combinations
from mpl_toolkits.mplot3d import Axes3D

import_file_Dframe  = 'Truth_Jet_Detector_Reference_Frame_Data/hgg_truth_jet_information.csv'
export_file_Dframe  = 'Truth_Jet_Detector_Reference_Frame_Data/hgg_truth_jet_information_4_bhad.csv'

import_file_Hframe  = 'Truth_Jet_Higgs_Reference_Frame_Data/hgg_truth_jet_information-Hframe.csv'
export_file_Hframe  = 'Truth_Jet_Higgs_Reference_Frame_Data/hgg_truth_jet_information_4_bhad_Hframe.csv'


# In[2]:


def angle_of_separation(pt_a,eta_a,phi_a,pt_b,eta_b,phi_b):
    angle = (math.acos(((pt_a*math.cos(phi_a))*(pt_b*math.cos(phi_b))+(pt_a*math.sin(phi_a))*(pt_b*math.sin(phi_b))+(pt_a*math.sinh(eta_a))*(pt_b*math.sinh(eta_b)))/((pt_a*math.cosh(eta_a))*(pt_b*math.cosh(eta_b)))))*180/math.pi
    return angle


# In[4]:


#Using pandas library to read in the data file and assign an array for the values of each column of the .csv file
file_lists = [import_file_Dframe,import_file_Hframe]

for i in range(len(file_lists)):
    data = pd.read_csv(file_lists[i])

    #This list contains all the named columns in the data file, each is a specific kinematic element generated for the data
    data_input_labels = ["tj_E","tj_pt","tj_eta","tj_phi","nbhad",
                         "bhad1_E","bhad1_pt","bhad1_eta","bhad1_phi",
                         "bhad2_E","bhad2_pt","bhad2_eta","bhad2_phi",
                         "bhad3_E","bhad3_pt","bhad3_eta","bhad3_phi",
                         "bhad4_E","bhad4_pt","bhad4_eta","bhad4_phi"]
    data_input_values = []
    data_kinematic_generated_labels = ["event_ID","target_ID","nbhad","tj_E","tj_pt","tj_px","tj_py","tj_pz","tj_p","tj_eta","tj_phi",
                                       "bhad1_E","bhad1_pt","bhad1_px","bhad1_py","bhad1_pz","bhad1_p","bhad1_eta","bhad1_phi",
                                       "bhad2_E","bhad2_pt","bhad2_px","bhad2_py","bhad2_pz","bhad2_p","bhad2_eta","bhad2_phi",
                                       "bhad3_E","bhad3_pt","bhad3_px","bhad3_py","bhad3_pz","bhad3_p","bhad3_eta","bhad3_phi",
                                       "bhad4_E","bhad4_pt","bhad4_px","bhad4_py","bhad4_pz","bhad4_p","bhad4_eta","bhad4_phi",
                                       "angle12","angle13","angle14","angle23","angle24","angle34"] 
    data_kinematic_generated_values = []

    for j in range(len(data_input_labels)):
        data_input_values.append(data[data_input_labels[j]])
    
    desired_nbhad_count = 4 #If this number is changed from any number other than 4, the kinematic labels and list calls need to be changed as well
    for j in range(len(data)):
        if(data_input_values[4][j] == desired_nbhad_count):
            data_list = [j,1,desired_nbhad_count,data_input_values[0][j],data_input_values[1][j],data_input_values[1][j]*math.cos(data_input_values[3][j]),data_input_values[1][j]*math.sin(data_input_values[3][j]),data_input_values[1][j]*math.sinh(data_input_values[2][j]),data_input_values[1][j]*math.cosh(data_input_values[2][j]),data_input_values[2][j],data_input_values[3][j],data_input_values[5][j],data_input_values[6][j],data_input_values[6][j]*math.cos(data_input_values[8][j]),data_input_values[6][j]*math.sin(data_input_values[8][j]),data_input_values[6][j]*math.sinh(data_input_values[7][j]),data_input_values[6][j]*math.cosh(data_input_values[7][j]),data_input_values[7][j],data_input_values[8][j],data_input_values[9][j],data_input_values[10][j],data_input_values[10][j]*math.cos(data_input_values[12][j]),data_input_values[10][j]*math.sin(data_input_values[12][j]),data_input_values[10][j]*math.sinh(data_input_values[11][j]),data_input_values[10][j]*math.cosh(data_input_values[11][j]),data_input_values[11][j],data_input_values[12][j],data_input_values[13][j],data_input_values[14][j],data_input_values[14][j]*math.cos(data_input_values[16][j]),data_input_values[14][j]*math.sin(data_input_values[16][j]),data_input_values[14][j]*math.sinh(data_input_values[15][j]),data_input_values[14][j]*math.cosh(data_input_values[15][j]),data_input_values[15][j],data_input_values[16][j],data_input_values[17][j],data_input_values[18][j],data_input_values[18][j]*math.cos(data_input_values[20][j]),data_input_values[18][j]*math.sin(data_input_values[20][j]),data_input_values[18][j]*math.sinh(data_input_values[19][j]),data_input_values[18][j]*math.cosh(data_input_values[19][j]),data_input_values[19][j],data_input_values[20][j],angle_of_separation(data_input_values[6][j],data_input_values[7][j],data_input_values[8][j],data_input_values[10][j],data_input_values[11][j],data_input_values[12][j]),angle_of_separation(data_input_values[6][j],data_input_values[7][j],data_input_values[8][j],data_input_values[14][j],data_input_values[15][j],data_input_values[16][j]),angle_of_separation(data_input_values[6][j],data_input_values[7][j],data_input_values[8][j],data_input_values[18][j],data_input_values[19][j],data_input_values[20][j]),angle_of_separation(data_input_values[10][j],data_input_values[11][j],data_input_values[12][j],data_input_values[14][j],data_input_values[15][j],data_input_values[16][j]),angle_of_separation(data_input_values[10][j],data_input_values[11][j],data_input_values[12][j],data_input_values[18][j],data_input_values[19][j],data_input_values[20][j]),angle_of_separation(data_input_values[14][j],data_input_values[15][j],data_input_values[16][j],data_input_values[18][j],data_input_values[19][j],data_input_values[20][j])] #Angle information
            data_kinematic_generated_values.append(data_list)
            
    kinematic_4bhad_data = pd.DataFrame(data_kinematic_generated_values, columns=data_kinematic_generated_labels)
    print(kinematic_4bhad_data)
    
    #if(i == 0):
        #kinematic_4bhad_data.to_csv(export_file_Dframe)
    #else if(i == 1):
        #kinematic_4bhad_data.to_csv(export_file_Hframe)


# In[ ]:




