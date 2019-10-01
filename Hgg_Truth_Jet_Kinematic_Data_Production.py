import pandas as pd 
import math

import_file_Dframe  = 'hgg_truth_jet_information.csv' #File that contains the raw kinematic data available, Dframe refers to Detector Frame
export_file_Dframe  = 'hgg_truth_jet_information_4_bhad.csv' #File that will contain the raw kinematic data available and any user-generated manipulations

import_file_Hframe  = 'hgg_truth_jet_information-Hframe.csv' #File that contains the raw kinematic data available, Hframe refers to Higgs Frame
export_file_Hframe  = 'hgg_truth_jet_information_4_bhad_Hframe.csv' #File that will contain the raw kinematic data available and any user-generated manipulations

#Function to generate the angle of separation between any two particle-jets
def angle_of_separation(pt_a,eta_a,phi_a,pt_b,eta_b,phi_b):
    angle = (math.acos(((pt_a*math.cos(phi_a))*(pt_b*math.cos(phi_b))+(pt_a*math.sin(phi_a))*(pt_b*math.sin(phi_b))+(pt_a*math.sinh(eta_a))*(pt_b*math.sinh(eta_b)))/((pt_a*math.cosh(eta_a))*(pt_b*math.cosh(eta_b)))))*180/math.pi
    return angle

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
    #This list contains all the named columns of data that this code can generate, to add more data, simply add on a column at the end
    data_kinematic_generated_labels = ["event_ID","target_ID","nbhad","tj_E","tj_pt","tj_px","tj_py","tj_pz","tj_p","tj_eta","tj_phi",
                                       "bhad1_E","bhad1_pt","bhad1_px","bhad1_py","bhad1_pz","bhad1_p","bhad1_eta","bhad1_phi",
                                       "bhad2_E","bhad2_pt","bhad2_px","bhad2_py","bhad2_pz","bhad2_p","bhad2_eta","bhad2_phi",
                                       "bhad3_E","bhad3_pt","bhad3_px","bhad3_py","bhad3_pz","bhad3_p","bhad3_eta","bhad3_phi",
                                       "bhad4_E","bhad4_pt","bhad4_px","bhad4_py","bhad4_pz","bhad4_p","bhad4_eta","bhad4_phi",
                                       "angle12","angle13","angle14","angle23","angle24","angle34"] 
    data_kinematic_generated_values = []

    #This loop populates an empty two-dimensional array with all the initial kinematic data, makes calling specific columns of data easier
    for j in range(len(data_input_labels)):
        data_input_values.append(data[data_input_labels[j]])
    
    desired_nbhad_count = 4 #If this number is changed from any number other than 4, the kinematic labels and list calls need to be changed as well
    
    #This loop searches for any event in the data that has the desired number of bhads produced then calculates the kinematic information to generate
    for j in range(len(data)):
        if(data_input_values[4][j] == desired_nbhad_count):
            #Heads up, the next line is massive, it contains the assignment of all kinematic values that are generated (which is currently 42 distinct kinematic elements)
            data_list = [j,1,desired_nbhad_count,data_input_values[0][j],data_input_values[1][j],data_input_values[1][j]*math.cos(data_input_values[3][j]),data_input_values[1][j]*math.sin(data_input_values[3][j]),data_input_values[1][j]*math.sinh(data_input_values[2][j]),data_input_values[1][j]*math.cosh(data_input_values[2][j]),data_input_values[2][j],data_input_values[3][j],data_input_values[5][j],data_input_values[6][j],data_input_values[6][j]*math.cos(data_input_values[8][j]),data_input_values[6][j]*math.sin(data_input_values[8][j]),data_input_values[6][j]*math.sinh(data_input_values[7][j]),data_input_values[6][j]*math.cosh(data_input_values[7][j]),data_input_values[7][j],data_input_values[8][j],data_input_values[9][j],data_input_values[10][j],data_input_values[10][j]*math.cos(data_input_values[12][j]),data_input_values[10][j]*math.sin(data_input_values[12][j]),data_input_values[10][j]*math.sinh(data_input_values[11][j]),data_input_values[10][j]*math.cosh(data_input_values[11][j]),data_input_values[11][j],data_input_values[12][j],data_input_values[13][j],data_input_values[14][j],data_input_values[14][j]*math.cos(data_input_values[16][j]),data_input_values[14][j]*math.sin(data_input_values[16][j]),data_input_values[14][j]*math.sinh(data_input_values[15][j]),data_input_values[14][j]*math.cosh(data_input_values[15][j]),data_input_values[15][j],data_input_values[16][j],data_input_values[17][j],data_input_values[18][j],data_input_values[18][j]*math.cos(data_input_values[20][j]),data_input_values[18][j]*math.sin(data_input_values[20][j]),data_input_values[18][j]*math.sinh(data_input_values[19][j]),data_input_values[18][j]*math.cosh(data_input_values[19][j]),data_input_values[19][j],data_input_values[20][j],angle_of_separation(data_input_values[6][j],data_input_values[7][j],data_input_values[8][j],data_input_values[10][j],data_input_values[11][j],data_input_values[12][j]),angle_of_separation(data_input_values[6][j],data_input_values[7][j],data_input_values[8][j],data_input_values[14][j],data_input_values[15][j],data_input_values[16][j]),angle_of_separation(data_input_values[6][j],data_input_values[7][j],data_input_values[8][j],data_input_values[18][j],data_input_values[19][j],data_input_values[20][j]),angle_of_separation(data_input_values[10][j],data_input_values[11][j],data_input_values[12][j],data_input_values[14][j],data_input_values[15][j],data_input_values[16][j]),angle_of_separation(data_input_values[10][j],data_input_values[11][j],data_input_values[12][j],data_input_values[18][j],data_input_values[19][j],data_input_values[20][j]),angle_of_separation(data_input_values[14][j],data_input_values[15][j],data_input_values[16][j],data_input_values[18][j],data_input_values[19][j],data_input_values[20][j])] #Angle information
            data_kinematic_generated_values.append(data_list)
            
    #This is a pandas DataFrame table; each row is a different event with the desired number of bhad and all other relevant kinematic info
    kinematic_4bhad_data = pd.DataFrame(data_kinematic_generated_values, columns=data_kinematic_generated_labels)
    
    if(i == 0):
        kinematic_4bhad_data.to_csv(export_file_Dframe)
    else if(i == 1):
        kinematic_4bhad_data.to_csv(export_file_Hframe)
