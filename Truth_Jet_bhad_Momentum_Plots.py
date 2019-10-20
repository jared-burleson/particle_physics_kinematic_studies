#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from itertools import combinations
from mpl_toolkits.mplot3d import Axes3D

import_file_hgg_Dframe = 'Truth_Jet_Detector_Reference_Frame_Data/hgg_truth_jet_information_4_bhad.csv'
import_file_hbb_Dframe = 'Truth_Jet_Detector_Reference_Frame_Data/hbb_truth_jet_information_4_bhad.csv'

import_file_lists = [import_file_hgg_Dframe, import_file_hbb_Dframe]
savefig_file_lists = ["Truth_Jet_Detector_Reference_Frame_Plots/Hgg_Momentum_Vectors/Event","Truth_Jet_Detector_Reference_Frame_Plots/Hbb_Momentum_Vectors/Event"]
title_lists = ["Hgg","Hbb"]

for i in range(len(import_file_lists)):
    data = pd.read_csv(import_file_lists[i])
    
    for j in range(len(data)):
        #Plotting the 3d momentum vectors for each bhadron in an event with 4 bhadrons
        plt.clf()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot([0,data["bhad1_px"][j]],[0,data["bhad1_py"][j]],[0,data["bhad1_pz"][j]])
        ax.plot([0,data["bhad2_px"][j]],[0,data["bhad2_py"][j]],[0,data["bhad2_pz"][j]])
        ax.plot([0,data["bhad3_px"][j]],[0,data["bhad3_py"][j]],[0,data["bhad3_pz"][j]])
        ax.plot([0,data["bhad4_px"][j]],[0,data["bhad4_py"][j]],[0,data["bhad4_pz"][j]])
        ax.set_xlabel("Momentum (MeV) in X", rotation = 0)
        ax.set_ylabel("Momentum (MeV) in Y", rotation = 0)
        ax.set_zlabel("Momentum (MeV) in Z", rotation = 0)
        plt.title(str(title_lists[i]) + "Truth Jet Momentum Plot: Event #"+str(data["event_ID"][j]))
        plt.legend(('bhad1','bhad2','bhad3','bhad4'))
        fig.tight_layout()
        plt.savefig(str(savefig_file_lists[i])+str(data["event_ID"][j])+".png", dpi=300, bbox_inches='tight') #Saves figures out to a file path inside the main folder


# In[ ]:




