# Kinematic Study of Particle Physics Processes

**Note:** This is still a major work in progress. I am currently working on moving over my code to github and condensing it in a generally applicable form.

This project is a collection of python code useful in analyzing kinematics of HEP processes. 

The particular application of this code, of which I am currently working on, is the study of ![equation](https://latex.codecogs.com/png.latex?$\textit{H}^0&space;\rightarrow&space;gg&space;\rightarrow&space;b\overline{b}b\overline{b}$) 
against ![equation](https://latex.codecogs.com/png.latex?$\textit{H}^0&space;\rightarrow&space;b\overline{b}g&space;\rightarrow&space;b\overline{b}b\overline{b}$).

However, the goal of utilizing a github for my code is to generalize a process for studying kinematic data on any particular process in particle physics.

**To get started:**

This code is written in python, but nothing that is done in the code is particularly difficult. I am studying physics after all.
Nevertheless, a background or understanding of python is probably important to reading the code that is used.
The project itself is purely based on data science analysis so I mainly stick to using the most basic of python libraries with the addition of the pandas library class in order to help express large data in appropriate lists, as well as graphics libraries for later analysis.

**Purpose of each file:**

In order to do any kind of data analysis on the kinematics of a particle physics process, we need the actual data. Very insightful, I know.
The file that I have included is `test_hgg_event_data.csv`. This file contains 5 example events in rows with the columns being the input kinematic information that is useful for analysis.

/side_note 

> This is a extremely condensed version of the type of .csv file that is generated from a simulation. I haven't included any of the coding or methodology for the simulation nor the capturing/isolation of the data that I want, because that is a different topic than the analysis portion here. There is an insane amount of kinematic information avaliable through a simulation, and I have done my best to condense it down to study only factors that are particularly meaningful to my study at the moment. Any future study could contain more or less parameters based on the nature of the study, and thus should be adjusted at the discretion of the project.

/end side_note

This analysis can be done on more than one .csv file. In fact the code is generalized to handle a list of any number of .csv files. The only constraint is that each data file contain the same columns, meaning that the kinematic data to be analyzed should be the same and in the same order in each file in order to avoid errors.

Once all the necessary data .csv files have been generated, it's time to move on to the analysis. 
