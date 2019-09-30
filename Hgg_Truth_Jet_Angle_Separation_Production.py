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

import_file1  = 'Truth_Jet_Detector_Reference_Frame_Data/hgg_truth_jet_information.csv'
export_file1  = 'Truth_Jet_Detector_Reference_Frame_Data/hgg_truth_jet_information_4_bhad.csv'
export_file3  = 'Truth_Jet_Detector_Reference_Frame_Data/hgg_nbhad_frequency.csv'

import_file2  = 'Truth_Jet_Higgs_Reference_Frame_Data/hgg_truth_jet_information-Hframe.csv'
export_file2  = 'Truth_Jet_Higgs_Reference_Frame_Data/hgg_truth_jet_information_4_bhad_Hframe.csv'
export_file4  = 'Truth_Jet_Higgs_Reference_Frame_Data/hgg_nbhad_frequency_Hframe.csv'


# In[2]:


#Code for import_file1

#Using pandas library to read in the data file and assign an array for the values of each column of the .csv file
data = pd.read_csv(import_file1)
tj_E      = data["tj_E"]
tj_pt     = data["tj_pt"]
tj_eta    = data["tj_eta"]
tj_phi    = data["tj_phi"]
nbhad     = data["nbhad"]
bhad1_E   = data["bhad1_E"]
bhad1_pt  = data["bhad1_pt"]
bhad1_eta = data["bhad1_eta"]
bhad1_phi = data["bhad1_phi"]
bhad2_E   = data["bhad2_E"]
bhad2_pt  = data["bhad2_pt"]
bhad2_eta = data["bhad2_eta"]
bhad2_phi = data["bhad2_phi"]
bhad3_E   = data["bhad3_E"]
bhad3_pt  = data["bhad3_pt"]
bhad3_eta = data["bhad3_eta"]
bhad3_phi = data["bhad3_phi"]
bhad4_E   = data["bhad4_E"]
bhad4_pt  = data["bhad4_pt"]
bhad4_eta = data["bhad4_eta"]
bhad4_phi = data["bhad4_phi"]

#Empty arrays that will be filled with manipulations of values from the columns of the import_file
frequency            = [0,0,0,0,0,0]
adjusted_frequency   = [0,0,0,0,0,0]
event_ID             = []
target_ID_4bhad      = []
nbhad_4bhad          = []
tj_E_4bhad           = []
tj_pt_4bhad          = []
tj_px_4bhad          = []
tj_py_4bhad          = []
tj_pz_4bhad          = []
tj_p_4bhad           = []
tj_eta_4bhad         = []
tj_phi_4bhad         = []
bhad1_E_4bhad        = []
bhad1_pt_4bhad       = []
bhad1_px_4bhad       = []
bhad1_py_4bhad       = []
bhad1_pz_4bhad       = []
bhad1_p_4bhad        = []
bhad1_eta_4bhad      = []
bhad1_phi_4bhad      = []
bhad2_E_4bhad        = []
bhad2_pt_4bhad       = []
bhad2_px_4bhad       = []
bhad2_py_4bhad       = []
bhad2_pz_4bhad       = []
bhad2_p_4bhad        = []
bhad2_eta_4bhad      = []
bhad2_phi_4bhad      = []
bhad3_E_4bhad        = []
bhad3_pt_4bhad       = []
bhad3_px_4bhad       = []
bhad3_py_4bhad       = []
bhad3_pz_4bhad       = []
bhad3_p_4bhad        = []
bhad3_eta_4bhad      = []
bhad3_phi_4bhad      = []
bhad4_E_4bhad        = []
bhad4_pt_4bhad       = []
bhad4_px_4bhad       = []
bhad4_py_4bhad       = []
bhad4_pz_4bhad       = []
bhad4_p_4bhad        = []
bhad4_eta_4bhad      = []
bhad4_phi_4bhad      = []
angle12_4bhad        = []
angle13_4bhad        = []
angle14_4bhad        = []
angle23_4bhad        = []
angle24_4bhad        = []
angle34_4bhad        = []

#Recording in an array the frequency of each number of b-hadrons 
for a in range(len(data)):
    for b in range(len(frequency)):
        if(nbhad[a] == b):
            frequency[b]+=1

dataSet_frequency = {'Frequency':frequency}
table_frequency = pd.DataFrame(dataSet_frequency)
table_frequency.to_csv(export_file3)
            
print("Data for 4 b-hadron events:") #The following code is only for events that record 4 distinct b-hadrons in a jet

for i in range(len(data)):
    if(nbhad[i] == 4): #Identifying an event that had 4 b-hadrons in the jet, populating arrays with the data from .csv
        event_ID.append(i)
        target_ID_4bhad.append(1)
        nbhad_4bhad.append(4)
        tj_E_4bhad.append(tj_E[i])
        tj_pt_4bhad.append(tj_pt[i])
        tj_px_4bhad.append(tj_pt[i]*math.cos(tj_phi[i]))
        tj_py_4bhad.append(tj_pt[i]*math.sin(tj_phi[i]))
        tj_pz_4bhad.append(tj_pt[i]*math.sinh(tj_eta[i]))
        tj_p_4bhad.append(tj_pt[i]*math.cosh(tj_eta[i]))
        tj_eta_4bhad.append(tj_eta[i])
        tj_phi_4bhad.append(tj_phi[i])
        bhad1_E_4bhad.append(bhad1_E[i])
        bhad1_pt_4bhad.append(bhad1_pt[i])
        bhad1_px_4bhad.append(bhad1_pt[i]*math.cos(bhad1_phi[i]))
        bhad1_py_4bhad.append(bhad1_pt[i]*math.sin(bhad1_phi[i]))
        bhad1_pz_4bhad.append(bhad1_pt[i]*math.sinh(bhad1_eta[i]))
        bhad1_p_4bhad.append(bhad1_pt[i]*math.cosh(bhad1_eta[i]))
        bhad1_eta_4bhad.append(bhad1_eta[i])
        bhad1_phi_4bhad.append(bhad1_phi[i])
        bhad2_E_4bhad.append(bhad2_E[i])
        bhad2_pt_4bhad.append(bhad2_pt[i])
        bhad2_px_4bhad.append(bhad2_pt[i]*math.cos(bhad2_phi[i]))
        bhad2_py_4bhad.append(bhad2_pt[i]*math.sin(bhad2_phi[i]))
        bhad2_pz_4bhad.append(bhad2_pt[i]*math.sinh(bhad2_eta[i]))
        bhad2_p_4bhad.append(bhad2_pt[i]*math.cosh(bhad2_eta[i]))
        bhad2_eta_4bhad.append(bhad2_eta[i])
        bhad2_phi_4bhad.append(bhad2_phi[i])
        bhad3_E_4bhad.append(bhad3_E[i])
        bhad3_pt_4bhad.append(bhad3_pt[i])
        bhad3_px_4bhad.append(bhad3_pt[i]*math.cos(bhad3_phi[i]))
        bhad3_py_4bhad.append(bhad3_pt[i]*math.sin(bhad3_phi[i]))
        bhad3_pz_4bhad.append(bhad3_pt[i]*math.sinh(bhad3_eta[i]))
        bhad3_p_4bhad.append(bhad3_pt[i]*math.cosh(bhad3_eta[i]))
        bhad3_eta_4bhad.append(bhad3_eta[i])
        bhad3_phi_4bhad.append(bhad3_phi[i])
        bhad4_E_4bhad.append(bhad4_E[i])
        bhad4_pt_4bhad.append(bhad4_pt[i])
        bhad4_px_4bhad.append(bhad4_pt[i]*math.cos(bhad4_phi[i]))
        bhad4_py_4bhad.append(bhad4_pt[i]*math.sin(bhad4_phi[i]))
        bhad4_pz_4bhad.append(bhad4_pt[i]*math.sinh(bhad4_eta[i]))
        bhad4_p_4bhad.append(bhad4_pt[i]*math.cosh(bhad4_eta[i]))
        bhad4_eta_4bhad.append(bhad4_eta[i])
        bhad4_phi_4bhad.append(bhad4_phi[i])

for i in range(len(target_ID_4bhad)):
    #Calculating Angle of Separation between bhadrons in an event with 4 bhadrons, based on index location of bhadron
    angle12_4bhad.append((math.acos(((bhad1_px_4bhad[i]*bhad2_px_4bhad[i])+(bhad1_py_4bhad[i]*bhad2_py_4bhad[i])+(bhad1_pz_4bhad[i]*bhad2_pz_4bhad[i]))/(bhad1_p_4bhad[i]*bhad2_p_4bhad[i])))*180/math.pi)
    angle13_4bhad.append((math.acos(((bhad1_px_4bhad[i]*bhad3_px_4bhad[i])+(bhad1_py_4bhad[i]*bhad3_py_4bhad[i])+(bhad1_pz_4bhad[i]*bhad3_pz_4bhad[i]))/(bhad1_p_4bhad[i]*bhad3_p_4bhad[i])))*180/math.pi)
    angle14_4bhad.append((math.acos(((bhad1_px_4bhad[i]*bhad4_px_4bhad[i])+(bhad1_py_4bhad[i]*bhad4_py_4bhad[i])+(bhad1_pz_4bhad[i]*bhad4_pz_4bhad[i]))/(bhad1_p_4bhad[i]*bhad4_p_4bhad[i])))*180/math.pi)
    angle23_4bhad.append((math.acos(((bhad2_px_4bhad[i]*bhad3_px_4bhad[i])+(bhad2_py_4bhad[i]*bhad3_py_4bhad[i])+(bhad2_pz_4bhad[i]*bhad3_pz_4bhad[i]))/(bhad2_p_4bhad[i]*bhad3_p_4bhad[i])))*180/math.pi)
    angle24_4bhad.append((math.acos(((bhad2_px_4bhad[i]*bhad4_px_4bhad[i])+(bhad2_py_4bhad[i]*bhad4_py_4bhad[i])+(bhad2_pz_4bhad[i]*bhad4_pz_4bhad[i]))/(bhad2_p_4bhad[i]*bhad4_p_4bhad[i])))*180/math.pi)
    angle34_4bhad.append((math.acos(((bhad3_px_4bhad[i]*bhad4_px_4bhad[i])+(bhad3_py_4bhad[i]*bhad4_py_4bhad[i])+(bhad3_pz_4bhad[i]*bhad4_pz_4bhad[i]))/(bhad3_p_4bhad[i]*bhad4_p_4bhad[i])))*180/math.pi)
    
    #Plotting the 3d momentum vectors for each bhadron in an event with 4 bhadrons
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([0,bhad1_px_4bhad[i]],[0,bhad1_py_4bhad[i]],[0,bhad1_pz_4bhad[i]])
    ax.plot([0,bhad2_px_4bhad[i]],[0,bhad2_py_4bhad[i]],[0,bhad2_pz_4bhad[i]])
    ax.plot([0,bhad3_px_4bhad[i]],[0,bhad3_py_4bhad[i]],[0,bhad3_pz_4bhad[i]])
    ax.plot([0,bhad4_px_4bhad[i]],[0,bhad4_py_4bhad[i]],[0,bhad4_pz_4bhad[i]])
    ax.set_xlabel("Momentum (MeV) in X", rotation = 0)
    ax.set_ylabel("Momentum (MeV) in Y", rotation = 0)
    ax.set_zlabel("Momentum (MeV) in Z", rotation = 0)
    plt.title("Hgg Truth Jet Momentum Plot: Event #"+str(event_ID[i]))
    plt.legend(('bhad1','bhad2','bhad3','bhad4'))
    fig.tight_layout()
    plt.savefig("Truth_Jet_Detector_Reference_Frame_Plots/Hgg_Momentum_Vectors/Event"+str(event_ID[i])+".png", dpi=300, bbox_inches='tight') #Saves figures out to a file path inside the main folder


# In[ ]:


#Code for import_file2

#Using pandas library to read in the data file and assign an array for the values of each column of the .csv file
data_Hframe = pd.read_csv(import_file2)
tj_E_Hframe      = data_Hframe["tj_E"]
tj_pt_Hframe     = data_Hframe["tj_pt"]
tj_eta_Hframe    = data_Hframe["tj_eta"]
tj_phi_Hframe    = data_Hframe["tj_phi"]
nbhad_Hframe     = data_Hframe["nbhad"]
bhad1_E_Hframe   = data_Hframe["bhad1_E"]
bhad1_pt_Hframe  = data_Hframe["bhad1_pt"]
bhad1_eta_Hframe = data_Hframe["bhad1_eta"]
bhad1_phi_Hframe = data_Hframe["bhad1_phi"]
bhad2_E_Hframe   = data_Hframe["bhad2_E"]
bhad2_pt_Hframe  = data_Hframe["bhad2_pt"]
bhad2_eta_Hframe = data_Hframe["bhad2_eta"]
bhad2_phi_Hframe = data_Hframe["bhad2_phi"]
bhad3_E_Hframe   = data_Hframe["bhad3_E"]
bhad3_pt_Hframe  = data_Hframe["bhad3_pt"]
bhad3_eta_Hframe = data_Hframe["bhad3_eta"]
bhad3_phi_Hframe = data_Hframe["bhad3_phi"]
bhad4_E_Hframe   = data_Hframe["bhad4_E"]
bhad4_pt_Hframe  = data_Hframe["bhad4_pt"]
bhad4_eta_Hframe = data_Hframe["bhad4_eta"]
bhad4_phi_Hframe = data_Hframe["bhad4_phi"]

#Empty arrays that will be filled with manipulations of values from the columns of the import_file
frequency_Hframe            = [0,0,0,0,0,0]
event_ID_Hframe             = []
target_ID_4bhad_Hframe      = []
nbhad_4bhad_Hframe          = []
tj_E_4bhad_Hframe           = []
tj_pt_4bhad_Hframe          = []
tj_px_4bhad_Hframe          = []
tj_py_4bhad_Hframe          = []
tj_pz_4bhad_Hframe          = []
tj_p_4bhad_Hframe           = []
tj_eta_4bhad_Hframe         = []
tj_phi_4bhad_Hframe         = []
bhad1_E_4bhad_Hframe        = []
bhad1_pt_4bhad_Hframe       = []
bhad1_px_4bhad_Hframe       = []
bhad1_py_4bhad_Hframe       = []
bhad1_pz_4bhad_Hframe       = []
bhad1_p_4bhad_Hframe        = []
bhad1_eta_4bhad_Hframe      = []
bhad1_phi_4bhad_Hframe      = []
bhad2_E_4bhad_Hframe        = []
bhad2_pt_4bhad_Hframe       = []
bhad2_px_4bhad_Hframe       = []
bhad2_py_4bhad_Hframe       = []
bhad2_pz_4bhad_Hframe       = []
bhad2_p_4bhad_Hframe        = []
bhad2_eta_4bhad_Hframe      = []
bhad2_phi_4bhad_Hframe      = []
bhad3_E_4bhad_Hframe        = []
bhad3_pt_4bhad_Hframe       = []
bhad3_px_4bhad_Hframe       = []
bhad3_py_4bhad_Hframe       = []
bhad3_pz_4bhad_Hframe       = []
bhad3_p_4bhad_Hframe        = []
bhad3_eta_4bhad_Hframe      = []
bhad3_phi_4bhad_Hframe      = []
bhad4_E_4bhad_Hframe        = []
bhad4_pt_4bhad_Hframe       = []
bhad4_px_4bhad_Hframe       = []
bhad4_py_4bhad_Hframe       = []
bhad4_pz_4bhad_Hframe       = []
bhad4_p_4bhad_Hframe        = []
bhad4_eta_4bhad_Hframe      = []
bhad4_phi_4bhad_Hframe      = []
angle12_4bhad_Hframe        = []
angle13_4bhad_Hframe        = []
angle14_4bhad_Hframe        = []
angle23_4bhad_Hframe        = []
angle24_4bhad_Hframe        = []
angle34_4bhad_Hframe        = []

#Recording in an array the frequency of each number of b-hadrons 
for a in range(len(data_Hframe)):
    for b in range(len(frequency_Hframe)):
        if(nbhad_Hframe[a] == b):
            frequency_Hframe[b]+=1

dataSet_frequency_Hframe = {'Frequency':frequency_Hframe}
table_frequency_Hframe = pd.DataFrame(dataSet_frequency_Hframe)
table_frequency_Hframe.to_csv(export_file4)

print("Data for 4 b-hadron events:") #The following code is only for events that record 4 distinct b-hadrons in a jet

for i in range(len(data_Hframe)):
    if(nbhad_Hframe[i] == 4): #Identifying an event that had 4 b-hadrons in the jet, populating arrays with the data from .csv
        event_ID_Hframe.append(i)
        target_ID_4bhad_Hframe.append(1)
        nbhad_4bhad_Hframe.append(4)
        tj_E_4bhad_Hframe.append(tj_E_Hframe[i])
        tj_pt_4bhad_Hframe.append(tj_pt_Hframe[i])
        tj_px_4bhad_Hframe.append(tj_pt_Hframe[i]*math.cos(tj_phi_Hframe[i]))
        tj_py_4bhad_Hframe.append(tj_pt_Hframe[i]*math.sin(tj_phi_Hframe[i]))
        tj_pz_4bhad_Hframe.append(tj_pt_Hframe[i]*math.sinh(tj_eta_Hframe[i]))
        tj_p_4bhad_Hframe.append(tj_pt_Hframe[i]*math.cosh(tj_eta_Hframe[i]))
        tj_eta_4bhad_Hframe.append(tj_eta_Hframe[i])
        tj_phi_4bhad_Hframe.append(tj_phi_Hframe[i])
        bhad1_E_4bhad_Hframe.append(bhad1_E_Hframe[i])
        bhad1_pt_4bhad_Hframe.append(bhad1_pt_Hframe[i])
        bhad1_px_4bhad_Hframe.append(bhad1_pt_Hframe[i]*math.cos(bhad1_phi_Hframe[i]))
        bhad1_py_4bhad_Hframe.append(bhad1_pt_Hframe[i]*math.sin(bhad1_phi_Hframe[i]))
        bhad1_pz_4bhad_Hframe.append(bhad1_pt_Hframe[i]*math.sinh(bhad1_eta_Hframe[i]))
        bhad1_p_4bhad_Hframe.append(bhad1_pt_Hframe[i]*math.cosh(bhad1_eta_Hframe[i]))
        bhad1_eta_4bhad_Hframe.append(bhad1_eta_Hframe[i])
        bhad1_phi_4bhad_Hframe.append(bhad1_phi_Hframe[i])
        bhad2_E_4bhad_Hframe.append(bhad2_E_Hframe[i])
        bhad2_pt_4bhad_Hframe.append(bhad2_pt_Hframe[i])
        bhad2_px_4bhad_Hframe.append(bhad2_pt_Hframe[i]*math.cos(bhad2_phi_Hframe[i]))
        bhad2_py_4bhad_Hframe.append(bhad2_pt_Hframe[i]*math.sin(bhad2_phi_Hframe[i]))
        bhad2_pz_4bhad_Hframe.append(bhad2_pt_Hframe[i]*math.sinh(bhad2_eta_Hframe[i]))
        bhad2_p_4bhad_Hframe.append(bhad2_pt_Hframe[i]*math.cosh(bhad2_eta_Hframe[i]))
        bhad2_eta_4bhad_Hframe.append(bhad2_eta_Hframe[i])
        bhad2_phi_4bhad_Hframe.append(bhad2_phi_Hframe[i])
        bhad3_E_4bhad_Hframe.append(bhad3_E_Hframe[i])
        bhad3_pt_4bhad_Hframe.append(bhad3_pt_Hframe[i])
        bhad3_px_4bhad_Hframe.append(bhad3_pt_Hframe[i]*math.cos(bhad3_phi_Hframe[i]))
        bhad3_py_4bhad_Hframe.append(bhad3_pt_Hframe[i]*math.sin(bhad3_phi_Hframe[i]))
        bhad3_pz_4bhad_Hframe.append(bhad3_pt_Hframe[i]*math.sinh(bhad3_eta_Hframe[i]))
        bhad3_p_4bhad_Hframe.append(bhad3_pt_Hframe[i]*math.cosh(bhad3_eta_Hframe[i]))
        bhad3_eta_4bhad_Hframe.append(bhad3_eta_Hframe[i])
        bhad3_phi_4bhad_Hframe.append(bhad3_phi_Hframe[i])
        bhad4_E_4bhad_Hframe.append(bhad4_E_Hframe[i])
        bhad4_pt_4bhad_Hframe.append(bhad4_pt_Hframe[i])
        bhad4_px_4bhad_Hframe.append(bhad4_pt_Hframe[i]*math.cos(bhad4_phi_Hframe[i]))
        bhad4_py_4bhad_Hframe.append(bhad4_pt_Hframe[i]*math.sin(bhad4_phi_Hframe[i]))
        bhad4_pz_4bhad_Hframe.append(bhad4_pt_Hframe[i]*math.sinh(bhad4_eta_Hframe[i]))
        bhad4_p_4bhad_Hframe.append(bhad4_pt_Hframe[i]*math.cosh(bhad4_eta_Hframe[i]))
        bhad4_eta_4bhad_Hframe.append(bhad4_eta_Hframe[i])
        bhad4_phi_4bhad_Hframe.append(bhad4_phi_Hframe[i])

for i in range(len(target_ID_4bhad_Hframe)):
    #Calculating Angle of Separation between bhadrons in an event with 4 bhadrons, based on index location of bhadron
    angle12_4bhad_Hframe.append((math.acos(((bhad1_px_4bhad_Hframe[i]*bhad2_px_4bhad_Hframe[i])+(bhad1_py_4bhad_Hframe[i]*bhad2_py_4bhad_Hframe[i])+(bhad1_pz_4bhad_Hframe[i]*bhad2_pz_4bhad_Hframe[i]))/(bhad1_p_4bhad_Hframe[i]*bhad2_p_4bhad_Hframe[i])))*180/math.pi)
    angle13_4bhad_Hframe.append((math.acos(((bhad1_px_4bhad_Hframe[i]*bhad3_px_4bhad_Hframe[i])+(bhad1_py_4bhad_Hframe[i]*bhad3_py_4bhad_Hframe[i])+(bhad1_pz_4bhad_Hframe[i]*bhad3_pz_4bhad_Hframe[i]))/(bhad1_p_4bhad_Hframe[i]*bhad3_p_4bhad_Hframe[i])))*180/math.pi)
    angle14_4bhad_Hframe.append((math.acos(((bhad1_px_4bhad_Hframe[i]*bhad4_px_4bhad_Hframe[i])+(bhad1_py_4bhad_Hframe[i]*bhad4_py_4bhad_Hframe[i])+(bhad1_pz_4bhad_Hframe[i]*bhad4_pz_4bhad_Hframe[i]))/(bhad1_p_4bhad_Hframe[i]*bhad4_p_4bhad_Hframe[i])))*180/math.pi)
    angle23_4bhad_Hframe.append((math.acos(((bhad2_px_4bhad_Hframe[i]*bhad3_px_4bhad_Hframe[i])+(bhad2_py_4bhad_Hframe[i]*bhad3_py_4bhad_Hframe[i])+(bhad2_pz_4bhad_Hframe[i]*bhad3_pz_4bhad_Hframe[i]))/(bhad2_p_4bhad_Hframe[i]*bhad3_p_4bhad_Hframe[i])))*180/math.pi)
    angle24_4bhad_Hframe.append((math.acos(((bhad2_px_4bhad_Hframe[i]*bhad4_px_4bhad_Hframe[i])+(bhad2_py_4bhad_Hframe[i]*bhad4_py_4bhad_Hframe[i])+(bhad2_pz_4bhad_Hframe[i]*bhad4_pz_4bhad_Hframe[i]))/(bhad2_p_4bhad_Hframe[i]*bhad4_p_4bhad_Hframe[i])))*180/math.pi)
    angle34_4bhad_Hframe.append((math.acos(((bhad3_px_4bhad_Hframe[i]*bhad4_px_4bhad_Hframe[i])+(bhad3_py_4bhad_Hframe[i]*bhad4_py_4bhad_Hframe[i])+(bhad3_pz_4bhad_Hframe[i]*bhad4_pz_4bhad_Hframe[i]))/(bhad3_p_4bhad_Hframe[i]*bhad4_p_4bhad_Hframe[i])))*180/math.pi)
    
    #Plotting the 3d momentum vectors for each bhadron in an event with 4 bhadrons
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([0,bhad1_px_4bhad_Hframe[i]],[0,bhad1_py_4bhad_Hframe[i]],[0,bhad1_pz_4bhad_Hframe[i]])
    ax.plot([0,bhad2_px_4bhad_Hframe[i]],[0,bhad2_py_4bhad_Hframe[i]],[0,bhad2_pz_4bhad_Hframe[i]])
    ax.plot([0,bhad3_px_4bhad_Hframe[i]],[0,bhad3_py_4bhad_Hframe[i]],[0,bhad3_pz_4bhad_Hframe[i]])
    ax.plot([0,bhad4_px_4bhad_Hframe[i]],[0,bhad4_py_4bhad_Hframe[i]],[0,bhad4_pz_4bhad_Hframe[i]])
    ax.set_xlabel("Momentum (MeV) in X", rotation = 0)
    ax.set_ylabel("Momentum (MeV) in Y", rotation = 0)
    ax.set_zlabel("Momentum (MeV) in Z", rotation = 0)
    plt.title("Hgg Truth Jet Momentum Plot: Event #"+str(event_ID_Hframe[i]))
    plt.legend(('bhad1','bhad2','bhad3','bhad4'))
    fig.tight_layout()
    plt.savefig("Truth_Jet_Higgs_Reference_Frame_Plots/Hframe_Hgg_Momentum_Vectors/Event"+str(event_ID_Hframe[i])+".png", dpi=300, bbox_inches='tight') #Saves figures out to a file path inside the main folder


# In[ ]:


print(frequency)
print(frequency_Hframe)

#Hgg Detector Frame Files
dataSet1 = {'target_ID':target_ID_4bhad,'nbhad':nbhad_4bhad,'tj_E':tj_E_4bhad,'tj_pt':tj_pt_4bhad,'tj_px':tj_px_4bhad,
            'tj_py':tj_py_4bhad,'tj_pz':tj_pz_4bhad,'tj_p':tj_p_4bhad,'tj_eta':tj_eta_4bhad,'tj_phi':tj_phi_4bhad,
            'bhad1_E':bhad1_E_4bhad,'bhad1_pt':bhad1_pt_4bhad,'bhad1_px':bhad1_px_4bhad,'bhad1_py':bhad1_py_4bhad,'bhad1_pz':bhad1_pz_4bhad,
            'bhad1_p':bhad1_p_4bhad,'bhad1_eta':bhad1_eta_4bhad,'bhad1_phi':bhad1_phi_4bhad,
            'bhad2_E':bhad2_E_4bhad,'bhad2_pt':bhad2_pt_4bhad,'bhad2_px':bhad2_px_4bhad,'bhad2_py':bhad2_py_4bhad,'bhad2_pz':bhad2_pz_4bhad,
            'bhad2_p':bhad2_p_4bhad,'bhad2_eta':bhad2_eta_4bhad,'bhad2_phi':bhad2_phi_4bhad,
            'bhad3_E':bhad3_E_4bhad,'bhad3_pt':bhad3_pt_4bhad,'bhad3_px':bhad3_px_4bhad,'bhad3_py':bhad3_py_4bhad,'bhad3_pz':bhad3_pz_4bhad,
            'bhad3_p':bhad3_p_4bhad,'bhad3_eta':bhad3_eta_4bhad,'bhad3_phi':bhad3_phi_4bhad,
            'bhad4_E':bhad4_E_4bhad,'bhad4_pt':bhad4_pt_4bhad,'bhad4_px':bhad4_px_4bhad,'bhad4_py':bhad4_py_4bhad,'bhad4_pz':bhad4_pz_4bhad,
            'bhad4_p':bhad4_p_4bhad,'bhad4_eta':bhad4_eta_4bhad,'bhad4_phi':bhad4_phi_4bhad,
            'angle_12':angle12_4bhad,'angle_13':angle13_4bhad,'angle_14':angle14_4bhad,'angle_23':angle23_4bhad,
            'angle_24':angle24_4bhad,'angle_34':angle34_4bhad}
table1 = pd.DataFrame(dataSet1)
table1.to_csv(export_file1)

#Hgg Higgs Frame Files
dataSet2 = {'target_ID':target_ID_4bhad_Hframe,'nbhad':nbhad_4bhad_Hframe,'tj_E':tj_E_4bhad_Hframe,'tj_pt':tj_pt_4bhad_Hframe,
            'tj_px':tj_px_4bhad_Hframe,'tj_py':tj_py_4bhad_Hframe,'tj_pz':tj_pz_4bhad_Hframe,'tj_p':tj_p_4bhad_Hframe,'tj_eta':tj_eta_4bhad_Hframe,'tj_phi':tj_phi_4bhad_Hframe,
            'bhad1_E':bhad1_E_4bhad_Hframe,'bhad1_pt':bhad1_pt_4bhad_Hframe,'bhad1_px':bhad1_px_4bhad_Hframe,'bhad1_py':bhad1_py_4bhad_Hframe,'bhad1_pz':bhad1_pz_4bhad_Hframe,
            'bhad1_p':bhad1_p_4bhad_Hframe,'bhad1_eta':bhad1_eta_4bhad_Hframe,'bhad1_phi':bhad1_phi_4bhad_Hframe,
            'bhad2_E':bhad2_E_4bhad_Hframe,'bhad2_pt':bhad2_pt_4bhad_Hframe,'bhad2_px':bhad2_px_4bhad_Hframe,'bhad2_py':bhad2_py_4bhad_Hframe,'bhad2_pz':bhad2_pz_4bhad_Hframe,
            'bhad2_p':bhad2_p_4bhad_Hframe,'bhad2_eta':bhad2_eta_4bhad_Hframe,'bhad2_phi':bhad2_phi_4bhad_Hframe,
            'bhad3_E':bhad3_E_4bhad_Hframe,'bhad3_pt':bhad3_pt_4bhad_Hframe,'bhad3_px':bhad3_px_4bhad_Hframe,'bhad3_py':bhad3_py_4bhad_Hframe,'bhad3_pz':bhad3_pz_4bhad_Hframe,
            'bhad3_p':bhad3_p_4bhad_Hframe,'bhad3_eta':bhad3_eta_4bhad_Hframe,'bhad3_phi':bhad3_phi_4bhad_Hframe,
            'bhad4_E':bhad4_E_4bhad_Hframe,'bhad4_pt':bhad4_pt_4bhad_Hframe,'bhad4_px':bhad4_px_4bhad_Hframe,'bhad4_py':bhad4_py_4bhad_Hframe,'bhad4_pz':bhad4_pz_4bhad_Hframe,
            'bhad4_p':bhad4_p_4bhad_Hframe,'bhad4_eta':bhad4_eta_4bhad_Hframe,'bhad4_phi':bhad4_phi_4bhad_Hframe,
            'angle_12':angle12_4bhad_Hframe,'angle_13':angle13_4bhad_Hframe,'angle_14':angle14_4bhad_Hframe,'angle_23':angle23_4bhad_Hframe,
            'angle_24':angle24_4bhad_Hframe,'angle_34':angle34_4bhad_Hframe}
table2 = pd.DataFrame(dataSet2)
table2.to_csv(export_file2)


# In[ ]:




