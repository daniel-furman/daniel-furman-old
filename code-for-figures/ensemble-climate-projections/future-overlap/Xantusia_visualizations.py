#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 16:46:29 2020

@author: danielfurman
"""

# Script for error bar plot. Reveals uncertainty in habitat loss as a function
# of climate model (the error bars) and climate scenario (ssp) from WordClim
# CMIP6 models. 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

overlapped_stats = pd.read_csv('data-xant/overlapped_stats.csv', sep=',')
overlapped_stats.drop(['Unnamed: 0'], axis = 1, inplace = True )
overlapped_stats
overlapped_stats.loc[0,:] = overlapped_stats.loc[
    0,:] - overlapped_stats.loc[1,:]
overlapped_stats.loc[2,:] = overlapped_stats.loc[
    1,:] - overlapped_stats.loc[2,:] 
overlapped_stats.replace(0,np.nan, inplace = True)

fig, ax = plt.subplots()
x_time = [2048.5, 2068.5, 2088.5]
plt.errorbar(x_time,     overlapped_stats.loc[
    1,"ssp126_2041_2060":"ssp126_2081_2100"],
             yerr= [overlapped_stats.loc[
                 2,"ssp126_2041_2060":"ssp126_2081_2100"],
                    overlapped_stats.loc[
                        0,"ssp126_2041_2060":"ssp126_2081_2100"]],
                             fmt='o-.', color='green', ecolor='lightgray',
                             elinewidth=3, capsize=0,label = 'SSP 126');

x_time = [2049.5, 2069.5, 2089.5]
plt.errorbar(x_time,     overlapped_stats.loc[
    1,"ssp245_2041_2060":"ssp245_2081_2100"],
             yerr= [overlapped_stats.loc[
                 2,"ssp245_2041_2060":"ssp245_2081_2100"],
                    overlapped_stats.loc[
                        0,"ssp245_2041_2060":"ssp24_2081_2100"]],
                             fmt='o-.', color='black', ecolor='lightgray',
                             elinewidth=3, capsize=0, label = 'SSP 245');

x_time = [2050.5, 2070.5, 2090.5]

plt.errorbar(x_time,overlapped_stats.loc[
    1,"ssp370_2041_2060":"ssp370_2081_2100"],
             yerr=[overlapped_stats.loc[
                 2,"ssp370_2041_2060":"ssp370_2081_2100"],
                   overlapped_stats.loc[
                       0,"ssp370_2041_2060":"ssp370_2081_2100"]],
                             fmt='o-.', color='orange', ecolor='lightgray',
                                 elinewidth=3, capsize=0,label = 'SSP 370');
                                    

x_time = [2051.5, 2071.5, 2091.5]
plt.errorbar(x_time,     overlapped_stats.loc[
    1,"ssp585_2041_2060":"ssp585_2081_2100"],
             yerr=[overlapped_stats.loc[
                 2,"ssp585_2041_2060":"ssp585_2081_2100"],
                   overlapped_stats.loc[
                       0,"ssp585_2041_2060":"ssp585_2081_2100"]],
                         fmt='o-.', color='red', ecolor='lightgray',
                             elinewidth=3, capsize=0,label = 'SSP 585');

plt.title('Ensemble CMIP6 Climate Projections with \n Xantusia vigilis SDMs',
          weight = 'bold', size = 15)
plt.ylabel('Fraction projected' +
           '\n(intersection / current distribution)')
plt.xlabel('Mean of CMIP6 time period (years)')


ax.set_xticks([2050,2070,2090])
plt.legend(loc = 'lower left', shadow = True, fontsize = 7.80)
#plt.locator_params(axis='x', nbins=5)
#plt.savefig('images-xant/projections.png', dpi = 400)