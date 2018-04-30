#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 07:16:10 2018

@author: juan
"""
import csv

master2Dtable = [] 

with open("EdgarDataSet.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        master2Dtable.append(row)

# getting available data per year
        
import math
valid_per_year_table=[]
for row in range(0, len(master2Dtable)):  
#for row in range(0, 1): 
    row_data=[]
    row_data.append(master2Dtable[row][0]) # append company name    
    for year in range(0 , 10): 
        skip = year+1     
        nan_per_year=0
        for metric in range(1 , 9):
            if (math.isnan(float(master2Dtable[row][skip]))):
                nan_per_year += 1
            skip += 10
        row_data.append(((8-nan_per_year)/8)*100)
    valid_per_year_table.append(row_data)

# Calculate valid percentages for all years
validPerYear = []
for year in range(1,11):
    percent_50=0
    percent_60=0
    percent_70=0
    percent_80=0
    percent_90=0
    percent_100=0
    for company in range(0, len(valid_per_year_table)):
        if (valid_per_year_table[company][year] < 60):
            percent_50 +=1
        elif (valid_per_year_table[company][year] < 70):
            percent_60 +=1
        elif (valid_per_year_table[company][year] < 80):
            percent_70 +=1
        elif (valid_per_year_table[company][year] < 90):
            percent_80 +=1
        elif (valid_per_year_table[company][year] < 100):
            percent_90 +=1
        elif (valid_per_year_table[company][year] == 100):
            percent_100 +=1
    validPerYear.append(2007+year)
    validPerYear.append([percent_100,percent_90,percent_80,percent_70,percent_60,percent_50])   

# Valid percent for dataset 2012-2014
dataSetValidPecent = []
percent_50=0
percent_60=0
percent_70=0
percent_80=0
percent_90=0
percent_100=0
year_selected = 0
for year in range(0,3):
    if (year == 0):
        year_selected = 4
    if (year == 1):
        year_selected = 5
    if (year == 2):
        year_selected = 6
            
    for company in range(0, len(valid_per_year_table)):
        if (valid_per_year_table[company][year_selected] < 60):
            percent_50 +=1
        elif (valid_per_year_table[company][year_selected] < 70):
            percent_60 +=1
        elif (valid_per_year_table[company][year_selected] < 80):
            percent_70 +=1
        elif (valid_per_year_table[company][year_selected] < 90):
            percent_80 +=1
        elif (valid_per_year_table[company][year_selected] < 100):
            percent_90 +=1
        elif (valid_per_year_table[company][year_selected] == 100):
            percent_100 +=1

dataSetValidPecent.append([(percent_100/32409)*100,(percent_90/32409)*100,
                            (percent_80/32409)*100,(percent_70/32409)*100,
                            (percent_60/32409)*100,(percent_50/32409)*100])   

# Valid percent for dataset 2011-2014
dataSetValidPecent = []
percent_50=0
percent_60=0
percent_70=0
percent_80=0
percent_90=0
percent_100=0
year_selected = 0
for year in range(0,4):
    if (year == 0):
        year_selected = 4
    if (year == 1):
        year_selected = 5
    if (year == 2):
        year_selected = 6
    if (year == 2):
        year_selected = 3
            
    for company in range(0, len(valid_per_year_table)):
        if (valid_per_year_table[company][year_selected] < 60):
            percent_50 +=1
        elif (valid_per_year_table[company][year_selected] < 70):
            percent_60 +=1
        elif (valid_per_year_table[company][year_selected] < 80):
            percent_70 +=1
        elif (valid_per_year_table[company][year_selected] < 90):
            percent_80 +=1
        elif (valid_per_year_table[company][year_selected] < 100):
            percent_90 +=1
        elif (valid_per_year_table[company][year_selected] == 100):
            percent_100 +=1

dataSetValidPecent.append([(percent_100/43212)*100,(percent_90/43212)*100,
                            (percent_80/43212)*100,(percent_70/43212)*100,
                            (percent_60/43212)*100,(percent_50/43212)*100]) 