# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import calcbench as cb
import pandas as pd
pd.options.display.max_rows = 1000
%pylab inline

metrics = ['CurrentAssets',
                   'CurrentLiabilities', 
                   'Assets', 
                   'RetainedEarnings', 
                   'EBIT', 
                   'MarketCapAtEndOfPeriod',
                   'Liabilities',
                   'Revenue']
SIC_directory = {
        "Agriculture, Forestry, Fishing" : {
                "Agricultural Production - Crops" : 100,
                "Agricultural Production - LiveStock" : 200,
                "Agricultural Services" : 700,
                "Forestry" : 800,
                "Fishing, Huntig and Trapping" : 900
            },
        "Mining" : {
                "Oil And Gas Extraction" : 1300,
                "Metal Mining" : 1000,
                "Coal Mining" : 1200,
                "Mining Nonmetallic Minerals" : 1400
            },
        "Construction" : {
                "Building Construction General Contractors and Operative Builders" : 1500,
                "Heavy Construction other than Building Construction Contractors" : 1600,
                "Construction Special Trade Contractors" : 1700
            },
        "Manufacturing" : {
                "Food and Kindred Products" : 2000,
                "Tobacco Products" : 2100,
                "Textile Mill Products" : 2200,
                "Apparel and other Finished Products Made from Frabrics and Similar Materials" : 2300,
                "Lumber and Wood Products, except Furniture" : 2400,
                "Furniture and Fixtures" : 2500,
                "Paper and Allied Products" : 2600,
                "Printing, Publishing, and Allied Industries" : 2700,
                "Chemical and Allied Products" : 2800,
                "Petroleum Refining and Related Industries" : 2900,
                "Rubber and Miscellaneus Plastic Products" : 3000,
                "Leather and Leather Products" : 3100,
                "Stone, Clay, Glass, and Concrete Products" : 3200,
                "Primary Metal Industries" : 3300,
                "Fabricated Metal Products, except Machinery and Transportation Equipment" : 3400,
                "Industrial and Commercial Machinery and Computer Equipment" : 3500,
                "Electronic and other Electrical Equipment and Components, except Computer Equipment" : 3600,
                "Transportation Equipment": 3700,
                "Measuring, Analyzing, and Controlling Instruments; Photographic, Medical and Optical Goods; Watches and Clocks" : 3800,
                "Miscellaneous Manufacturing Industries" : 3900
                },
        "Transportation & Public Utilities" : {
                "Railroad Transportation" : 4000,
                "Local and Suburban Transit and Interurban Highway Passenger Transportation" : 4100,
                "Motor Freight Transportation and Warehousing" : 4200,
#                "United States Postal Service" : 4300,
                "Water Transportation" : 4400, 
                "Transportation by Air" : 4500,
                "Pipelines, except Natural Gas" : 4600,
                "Transportation Services" : 4700,
                "Communications" : 4800,
                "Electric, Gas and Sanitary Services" : 4900
                },
        "Wholesale Trade" : {
                "Wholesale Trade-Durable Goods" : 5000,
                "Wholesale Trade-Nondurable Goods" : 5100
                },
        "Retail Trade" : {
                "Building Materials, Hardware, Garden Supply, and Mobile Home Dealers" : 5200,
                "General Merchandise Stores": 5300,
                "Food Stores" : 5400,
                "Automotive Dealers and Gasoline Service Stations" : 5500,
                "Apparel and Accessory Stores" : 5600,
                "Home Furniture, Furnishings, and Equipment Stores" : 5700,
                "Eating and Drinking Places" : 5800,
                "Miscellaneous Retail" : 5900
                },
        "Finance, Insurance, Real State" : {
                "Depository Institutions": 6000,
                "Non-Depository Credit Institutions" : 6100,
                "Security and Commodity Brokers, Dealers, Exchanges, and Services" : 6200,
                "Insurance Carriers" : 6300,
                "Insurance Agents, Brokers and Service" : 6400,
                "Real Estate" : 6500,
                "Holding and other Investment Offices" : 6700
                },
        "Services" : {
                "Hotels, Rooming Houses, Camps, and other Lodging Places" : 7000,
                "Personal Services" : 7200,
                "Business Services" : 7300,
                "Automotive Repair, Services, and Parking" : 7500,
                "Miscellaneous Repair Services" : 7600,
                "Motion Pictures" : 7800,
                "Amusement and Recreation Services" : 7900,
                "Health Services" : 8000,
                "Legal Services" : 8100,
                "Educational Services" : 8200,
                "Social Services" : 8300,
#                "Museums, Art Galleries, and Botanical and Zoological Gardens" : 8400,
#                "Membership Organizations" : 8600,
                "Engineering, Accounting, Research, Management, and Related Services" : 8700,
#                "Private Households" : 8800,
                "Miscellaneous Services" : 8900
                },
        "Public Administration" : {
#                "Executive, Legislative, and General Government, except Finance" : 9100,
#                "Justice, Public Order, and Safety" : 9200,
#                "Public Finance, Taxation, and Monetary Policy" : 9300,
#                "Administration of Human Resource Programs" : 9400,
#                "Administration of Environmental Quality and Housing Programs" : 9500,
#                "Administration of Economic Programs" : 9600,
#                "National Security and International Affairs" : 9700,
                "Nonclassifiable Establishments" : 9900
                }
    }

def peer_group_data(peer_group):
    #peer group gets normalized
    normalized_data = cb.normalized_dataframe(company_identifiers=list(peer_group.ticker), 
                                           metrics=metrics, 
                                           start_year=2008, start_period=0, 
                                           end_year=2017, end_period=0)
    #peer group gets aggregated
    #aggregate_data = z_score_data.sum(level=[0], axis=1)
    return normalized_data


def master_data_sheet(SIC_codes):
    cb.set_credentials({'jma_usmc@hotmail.com'}, {'january14'})
    #creates list of all companies in each group and all of their data from cb.companies()
    peer_groups = [(industry, cb.companies(SIC_codes=[SIC_code])) for industry, SIC_code in SIC_codes.items()]

    #get list of 500 large-cap Us companies.
#    sp500 = cb.companies(index="SP500")

    industry_data = [(industry, peer_group_data(peer_group)) for industry, peer_group in peer_groups]
    
    return industry_data
    
masterDataSheet = [(industry, master_data_sheet(SIC_codes)) for industry, SIC_codes in SIC_directory.items()]
    
master2Dtable = []
for  classif in range(0, len(masterDataSheet)):
    for subClass in range(0, len(masterDataSheet[classif][1])):
        industryData = masterDataSheet[classif][1][subClass][1]
        company_names = list(industryData[metrics[0]])  
        for compName in range(0,len(company_names)):
            row = []
            row.append(company_names[compName])
            for metric in range(0,len(metrics)):
                metric_data = industryData[metrics[metric],company_names[compName]]
                for year in range(0, len(metric_data)):
                    row.append(metric_data[year])
            row.append(masterDataSheet[classif][0])
            master2Dtable.append(row)
            
           
master2Dtable = [(industry) for industry in master2Dtable if len(industry) == 82]

# Save CSV file
import csv
with open("MasterDataSheet.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(master2Dtable)
    
master2Dtable = [] 
with open("MasterDataSheet.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        master2Dtable.append(row)
    
import math
import numpy as numpy
nan_by_column = numpy.zeros([len(master2Dtable[0]),1])
for row in range(0, len(master2Dtable)):  
    for column in range(0, len(master2Dtable[row])):
        if column > 0 and column < 81:
                if (math.isnan(float(master2Dtable[row][column]))):
                    nan_by_column[column] = nan_by_column[column] + 1
percent_valid_per_column = [(((len(master2Dtable)-item)/len(master2Dtable))*100) for item in nan_by_column]       

index =1
by_metric=[]
for metric in range(0, len(metrics)):
    row=[]
    row.append(metrics[metric])
    year_taken = 2008    
    for year in range(1, 11): 
        row.append(year_taken)
        row.append(percent_valid_per_column[index])
        index = index + 1
        year_taken = year_taken+1
    by_metric.append(row)

nan_items = 0
nan_by_row = numpy.zeros([len(master2Dtable),1])
for row in range(0, len(master2Dtable)):
    for column in range(0, len(master2Dtable[row])):
        if column > 0 and column < 81:
            if (math.isnan(float(master2Dtable[row][column]))):
                nan_by_row[row] = nan_by_row[row] +1
percent_valid_per_row = [(((len(master2Dtable[0])-item)/len(master2Dtable[0]))*100) for item in nan_by_row]   