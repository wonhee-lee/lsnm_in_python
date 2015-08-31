# ============================================================================
#
#                            PUBLIC DOMAIN NOTICE
#
#       National Institute on Deafness and Other Communication Disorders
#
# This software/database is a "United States Government Work" under the 
# terms of the United States Copyright Act. It was written as part of 
# the author's official duties as a United States Government employee and 
# thus cannot be copyrighted. This software/database is freely available 
# to the public for use. The NIDCD and the U.S. Government have not placed 
# any restriction on its use or reproduction. 
#
# Although all reasonable efforts have been taken to ensure the accuracy 
# and reliability of the software and data, the NIDCD and the U.S. Government 
# do not and cannot warrant the performance or results that may be obtained 
# by using this software or data. The NIDCD and the U.S. Government disclaim 
# all warranties, express or implied, including warranties of performance, 
# merchantability or fitness for any particular purpose.
#
# Please cite the author in any work or product based on this material.
# 
# ==========================================================================



# ***************************************************************************
#
#   Large-Scale Neural Modeling software (LSNM)
#
#   Section on Brain Imaging and Modeling
#   Voice, Speech and Language Branch
#   National Institute on Deafness and Other Communication Disorders
#   National Institutes of Health
#
#   This file (func_conn_fmri_visual.py) was created on July 10, 2015.
#
#   Based in part on Matlab scripts by Horwitz et al.
#
#   Author: Antonio Ulloa
#
#   Last updated by Antonio Ulloa on August 13, 2015  
# **************************************************************************/

# func_conn_fmri_visual.py
#
# Calculate and plot functional connectivity (within-task time series correlation)
# of the BOLD timeseries in IT with the BOLD timeseries of all other simulated brain
# regions. It reads the BOLD time-series from a python data file (*.npy) and writes
# the correlation coefficients to an output data file (*.npy)

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

import math as m

from scipy.stats import poisson

# define the length of both each trial and the whole experiment
# in synaptic timesteps, as well as total number of trials
experiment_length = 3960
trial_length = 110
number_of_trials = 36

synaptic_timesteps = experiment_length

# define the name of the input file where the BOLD timeseries are contained
BOLD_ts_file = 'lsnm_bold_balloon.npy'

# define the name of the output file where the functional connectivity timeseries will be stored
func_conn_dms_file = 'corr_fmri_IT_vs_all_dms.npy'
func_conn_ctl_file = 'corr_fmri_IT_vs_all_ctl.npy'

# define an array with location of control trials, and another array
# with location of task-related trials, relative to
# an array that contains all trials (task-related trials included)
# because we lose two trials at the beginning of the fmri experiment, we
# are left with only one trial during the first DMS block
# Therefore, out of 36 trials total we were left with only 34 trials,
# each trial lasting approximately ~3 MR ticks (2.75)
control_trials = [3,4,5,9,10,11,15,16,17,21,22,23,27,28,29,33,34,35]
dms_trials =     [0,1,2,6,7,8,12,13,14,18,19,20,24,25,26,30,31,32]

# define neural synaptic time interval in seconds. The simulation data is collected
# one data point at synaptic intervals (10 simulation timesteps). Every simulation
# timestep is equivalent to 5 ms.
Ti = 0.005 * 10

# define constant needed for hemodynamic function (in milliseconds)
lambda_ = 6

# Total time of scanning experiment in seconds (timesteps X 5)
T = 198

# Time for one complete trial in milliseconds
Ttrial = 5.5

# the scanning happened every Tr interval below (in milliseconds). This
# is the time needed to sample hemodynamic activity to produce
# each fMRI image.
Tr = 2

# Construct a numpy array of time points
time_in_seconds = np.arange(0, T, Tr)

scanning_timescale = np.arange(0, synaptic_timesteps, synaptic_timesteps / (T/Tr))
synaptic_timescale = np.arange(0, synaptic_timesteps)

# open file containing BOLD time-series
BOLD_ts = np.load(BOLD_ts_file)

print BOLD_ts.shape

# now, we need to convolve the synaptic activity with the hemodynamic delay
# function to generate a BOLD signal and then bring it back to a synaptic
# timescale
v1_BOLD = BOLD_ts[0,:]
v4_BOLD = BOLD_ts[1,:]
it_BOLD = BOLD_ts[2,:]
d1_BOLD = BOLD_ts[3,:]
d2_BOLD = BOLD_ts[4,:]
fs_BOLD = BOLD_ts[5,:]
fr_BOLD = BOLD_ts[6,:]

###############################################################################
###############################################################################
# We need to downsample the BOLD signal at this point, before we do any
# more processing to it.
v1_BOLD = v1_BOLD[scanning_timescale]
v4_BOLD = v4_BOLD[scanning_timescale]
it_BOLD = it_BOLD[scanning_timescale]
d1_BOLD = d1_BOLD[scanning_timescale]
d2_BOLD = d2_BOLD[scanning_timescale]
fs_BOLD = fs_BOLD[scanning_timescale]
fr_BOLD = fr_BOLD[scanning_timescale]

# And now we scale it up 10 times its size, so that we can subdivide the arrays
# in equally sized subarrays
scanning_timescale_x_100 = np.arange(0, synaptic_timesteps, synaptic_timesteps / (T*100.0/Tr))
v1_BOLD = np.interp(scanning_timescale_x_100, scanning_timescale, v1_BOLD)
v4_BOLD = np.interp(scanning_timescale_x_100, scanning_timescale, v4_BOLD)
it_BOLD = np.interp(scanning_timescale_x_100, scanning_timescale, it_BOLD)
d1_BOLD = np.interp(scanning_timescale_x_100, scanning_timescale, d1_BOLD)
d2_BOLD = np.interp(scanning_timescale_x_100, scanning_timescale, d2_BOLD)
fs_BOLD = np.interp(scanning_timescale_x_100, scanning_timescale, fs_BOLD)
fr_BOLD = np.interp(scanning_timescale_x_100, scanning_timescale, fr_BOLD)

###############################################################################
###############################################################################

# remove first few scans from BOLD signal arrays (to eliminate edge effects from
# convolution during the first block of scans)
# Please note that arrays have to be divisible by the number of trials, i.e., the
# BOLD arrays have to be split after deleting the first few scans, which has to
# result in an equal division. 
v1_BOLD = np.delete(v1_BOLD, np.arange(432))
v4_BOLD = np.delete(v4_BOLD, np.arange(432))
it_BOLD = np.delete(it_BOLD, np.arange(432))
d1_BOLD = np.delete(d1_BOLD, np.arange(432))
d2_BOLD = np.delete(d2_BOLD, np.arange(432))
fs_BOLD = np.delete(fs_BOLD, np.arange(432))
fr_BOLD = np.delete(fr_BOLD, np.arange(432))

# Get rid of the control trials in the BOLD signal arrays,
# by separating the task-related trials and concatenating them
# together. Remember that each trial is a number of synaptic timesteps
# long.

# first, split the arrays into subarrays, each one containing a single trial
it_subarrays = np.split(it_BOLD, number_of_trials)
v1_subarrays = np.split(v1_BOLD, number_of_trials)
v4_subarrays = np.split(v4_BOLD, number_of_trials)
d1_subarrays = np.split(d1_BOLD, number_of_trials)
d2_subarrays = np.split(d2_BOLD, number_of_trials)
fs_subarrays = np.split(fs_BOLD, number_of_trials)
fr_subarrays = np.split(fr_BOLD, number_of_trials)

print len(it_subarrays[0])

# we get rid of the inter-trial interval for each and all trials (1 second at the
# end of each trial. 1 second = 50 array positions.
#it_subarrays = np.delete(it_subarrays, np.arange(212,262), axis=1)
#v1_subarrays = np.delete(v1_subarrays, np.arange(212,262), axis=1)
#v4_subarrays = np.delete(v4_subarrays, np.arange(212,262), axis=1)
#d1_subarrays = np.delete(d1_subarrays, np.arange(212,262), axis=1)
#d2_subarrays = np.delete(d2_subarrays, np.arange(212,262), axis=1)
#fs_subarrays = np.delete(fs_subarrays, np.arange(212,262), axis=1)
#fr_subarrays = np.delete(fr_subarrays, np.arange(212,262), axis=1)

# now, get rid of the control trials...
it_DMS_trials = np.delete(it_subarrays, control_trials, axis=0)
v1_DMS_trials = np.delete(v1_subarrays, control_trials, axis=0)
v4_DMS_trials = np.delete(v4_subarrays, control_trials, axis=0)
d1_DMS_trials = np.delete(d1_subarrays, control_trials, axis=0)
d2_DMS_trials = np.delete(d2_subarrays, control_trials, axis=0)
fs_DMS_trials = np.delete(fs_subarrays, control_trials, axis=0)
fr_DMS_trials = np.delete(fr_subarrays, control_trials, axis=0)

# ... and concatenate the task-related trials together
it_DMS_trials_ts = np.concatenate(it_DMS_trials)
v1_DMS_trials_ts = np.concatenate(v1_DMS_trials)
v4_DMS_trials_ts = np.concatenate(v4_DMS_trials)
d1_DMS_trials_ts = np.concatenate(d1_DMS_trials)
d2_DMS_trials_ts = np.concatenate(d2_DMS_trials)
fs_DMS_trials_ts = np.concatenate(fs_DMS_trials)
fr_DMS_trials_ts = np.concatenate(fr_DMS_trials)

# but also, get rid of the DMS task trials, to create arrays with only control trials
it_control_trials = np.delete(it_subarrays, dms_trials, axis=0)
v1_control_trials = np.delete(v1_subarrays, dms_trials, axis=0)
v4_control_trials = np.delete(v4_subarrays, dms_trials, axis=0)
d1_control_trials = np.delete(d1_subarrays, dms_trials, axis=0)
d2_control_trials = np.delete(d2_subarrays, dms_trials, axis=0)
fs_control_trials = np.delete(fs_subarrays, dms_trials, axis=0)
fr_control_trials = np.delete(fr_subarrays, dms_trials, axis=0)

# ... and concatenate the control task trials together
it_control_trials_ts = np.concatenate(it_control_trials)
v1_control_trials_ts = np.concatenate(v1_control_trials)
v4_control_trials_ts = np.concatenate(v4_control_trials)
d1_control_trials_ts = np.concatenate(d1_control_trials)
d2_control_trials_ts = np.concatenate(d2_control_trials)
fs_control_trials_ts = np.concatenate(fs_control_trials)
fr_control_trials_ts = np.concatenate(fr_control_trials)

# Calculate new synaptic timesteps and scanning timescale, as all BOLD arrays
# have been halved
#new_synaptic_timesteps = v1_DMS_trials_ts.size
#scanning_timescale = np.arange(0, new_synaptic_timesteps, new_synaptic_timesteps / (T/Tr))

# now, sample all BOLD arrays, DMS and control, to match the
# MRI scanning interval:
#v1_DMS_trials_ts = v1_DMS_trials_ts[scanning_timescale]
#v4_DMS_trials_ts = v4_DMS_trials_ts[scanning_timescale]
#it_DMS_trials_ts = it_DMS_trials_ts[scanning_timescale]
#d1_DMS_trials_ts = d1_DMS_trials_ts[scanning_timescale]
#d2_DMS_trials_ts = d2_DMS_trials_ts[scanning_timescale]
#fs_DMS_trials_ts = fs_DMS_trials_ts[scanning_timescale]
#fr_DMS_trials_ts = fr_DMS_trials_ts[scanning_timescale]
#v1_control_trials_ts = v1_control_trials_ts[scanning_timescale]
#v4_control_trials_ts = v4_control_trials_ts[scanning_timescale]
#it_control_trials_ts = it_control_trials_ts[scanning_timescale]
#d1_control_trials_ts = d1_control_trials_ts[scanning_timescale]
#d2_control_trials_ts = d2_control_trials_ts[scanning_timescale]
#fs_control_trials_ts = fs_control_trials_ts[scanning_timescale]
#fr_control_trials_ts = fr_control_trials_ts[scanning_timescale]

v1_BOLD_dms = v1_DMS_trials_ts
v4_BOLD_dms = v4_DMS_trials_ts
it_BOLD_dms = it_DMS_trials_ts
d1_BOLD_dms = d1_DMS_trials_ts
d2_BOLD_dms = d2_DMS_trials_ts
fs_BOLD_dms = fs_DMS_trials_ts
fr_BOLD_dms = fr_DMS_trials_ts

v1_BOLD_ctl = v1_control_trials_ts
v4_BOLD_ctl = v4_control_trials_ts
it_BOLD_ctl = it_control_trials_ts
d1_BOLD_ctl = d1_control_trials_ts
d2_BOLD_ctl = d2_control_trials_ts
fs_BOLD_ctl = fs_control_trials_ts
fr_BOLD_ctl = fr_control_trials_ts

# now, convert DMS and control timeseries into pandas timeseries, so we can analyze it
IT_dms_ts = pd.Series(it_BOLD_dms)
V1_dms_ts = pd.Series(v1_BOLD_dms)
V4_dms_ts = pd.Series(v4_BOLD_dms)
D1_dms_ts = pd.Series(d1_BOLD_dms)
D2_dms_ts = pd.Series(d2_BOLD_dms)
FS_dms_ts = pd.Series(fs_BOLD_dms)
FR_dms_ts = pd.Series(fr_BOLD_dms)

IT_ctl_ts = pd.Series(it_BOLD_ctl)
V1_ctl_ts = pd.Series(v1_BOLD_ctl)
V4_ctl_ts = pd.Series(v4_BOLD_ctl)
D1_ctl_ts = pd.Series(d1_BOLD_ctl)
D2_ctl_ts = pd.Series(d2_BOLD_ctl)
FS_ctl_ts = pd.Series(fs_BOLD_ctl)
FR_ctl_ts = pd.Series(fr_BOLD_ctl)


# ... and calculate the functional connectivity of IT with the other modules
funct_conn_it_v1_dms = IT_dms_ts.corr(V1_dms_ts)
funct_conn_it_v4_dms = IT_dms_ts.corr(V4_dms_ts)
funct_conn_it_d1_dms = IT_dms_ts.corr(D1_dms_ts)
funct_conn_it_d2_dms = IT_dms_ts.corr(D2_dms_ts)
funct_conn_it_fs_dms = IT_dms_ts.corr(FS_dms_ts)
funct_conn_it_fr_dms = IT_dms_ts.corr(FR_dms_ts)

funct_conn_it_v1_ctl = IT_ctl_ts.corr(V1_ctl_ts)
funct_conn_it_v4_ctl = IT_ctl_ts.corr(V4_ctl_ts)
funct_conn_it_d1_ctl = IT_ctl_ts.corr(D1_ctl_ts)
funct_conn_it_d2_ctl = IT_ctl_ts.corr(D2_ctl_ts)
funct_conn_it_fs_ctl = IT_ctl_ts.corr(FS_ctl_ts)
funct_conn_it_fr_ctl = IT_ctl_ts.corr(FR_ctl_ts)

func_conn_dms = np.array([funct_conn_it_v1_dms,funct_conn_it_v4_dms,
                          funct_conn_it_d1_dms,funct_conn_it_d2_dms,
                          funct_conn_it_fs_dms,funct_conn_it_fr_dms])
func_conn_ctl = np.array([funct_conn_it_v1_ctl,funct_conn_it_v4_ctl,
                          funct_conn_it_d1_ctl,funct_conn_it_d2_ctl,
                          funct_conn_it_fs_ctl,funct_conn_it_fr_ctl])

# now, save all correlation coefficients to a output files 
np.save(func_conn_dms_file, func_conn_dms)
np.save(func_conn_ctl_file, func_conn_ctl)

# define number of groups to plot
N = 2

# create a list of x locations for each group 
index = np.arange(N)            
width = 0.1                     # width of the bars

fig, ax = plt.subplots()

ax.set_ylim([0,1])

# now, group the values to be plotted by brain module
it_v1_corr = (funct_conn_it_v1_dms, funct_conn_it_v1_ctl)
it_v4_corr = (funct_conn_it_v4_dms, funct_conn_it_v4_ctl)
it_d1_corr = (funct_conn_it_d1_dms, funct_conn_it_d1_ctl)
it_d2_corr = (funct_conn_it_d2_dms, funct_conn_it_d2_ctl)
it_fs_corr = (funct_conn_it_fs_dms, funct_conn_it_fs_ctl)
it_fr_corr = (funct_conn_it_fr_dms, funct_conn_it_fr_ctl)

rects_v1 = ax.bar(index, it_v1_corr, width, color='purple', label='V1')

rects_v4 = ax.bar(index + width, it_v4_corr, width, color='darkred', label='V4')

rects_fs = ax.bar(index + width*2, it_fs_corr, width, color='lightyellow', label='FS')

rects_d1 = ax.bar(index + width*3, it_d1_corr, width, color='lightblue', label='D1')

rects_d2 = ax.bar(index + width*4, it_d2_corr, width, color='yellow', label='D2')

rects_fr = ax.bar(index + width*5, it_fr_corr, width, color='red', label='FR')

ax.set_title('FUNCTIONAL CONNECTIVITY OF IT WITH OTHER BRAIN REGIONS (fMRI)')

# get rid of x axis ticks and labels
ax.set_xticks([])

ax.set_xlabel('DMS TASK                                        CONTROL TASK')
ax.xaxis.set_label_coords(0.5, -0.025)

# Shrink current axis by 10% to make space for legend
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

# place a legend to the right of the figure
plt.legend(loc='center left', bbox_to_anchor=(1.02, .5))

# Show the plots on the screen
plt.show()
