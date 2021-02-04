#!/usr/bin/env python
# coding: utf-8

# In[52]:


#This Python 3.x script is for parsing csv files (containing a column of zip codes- column must be named 'zip') to 
# deterime distances from a set location (Johns Hopkins Center in Baltimore, MD in this example). The output is a new csv file that 
#contains a new column (distance_miles) which denotes the distances for all zip codes from the given location, as well as an
#interactive map saved to a html file in the same directory where the source and output .csv files exist.
#Rex Robichaux, Jan, 2021. rexmrobichaux@gmail.com

#import required python dependencies
import pandas as pd
import os
import numpy as np
import geopy.distance
from geopy.distance import geodesic
import folium
from folium.plugins import MarkerCluster

#Johns Hopkins Location in Baltimore- change as needed.
site_coords = (39.301, -76.575)

#Import All Zip Codes -with lat lon data
df = pd.read_csv (r'C:\ZipCodeDistance\Allzipcodes.csv')
print (df.head())

#Perform distance calculation (geodesic / straight line calculation taking into effect curved surface of the earth). 
#Add distance_miles column to dataframe.
def calc_distance(row, site_coords):
    patient_coords = (row['latitude'], row['longitude'])
    d = geopy.distance.geodesic(site_coords, patient_coords).mi
    return(d)

#Set distance calculation- the coordinates need to match the site_coords above.
df['distance_miles'] = df.apply(calc_distance, site_coords=(39.301, -76.575), axis=1)
print (df.head())

#Import list of zip codes from new / input csv file. File must have a column with zip codes named "zip"
df2 = pd.read_csv (r'C:\ZipCodeDistance\inputzips.csv')
print (df2.head())

#Create final dataframe based off of a merge (inner join) between the two dataframes off of the zip code values in each.
df_final = pd.merge(df.astype(str),df2.astype(str),on='zip')
print (df_final.head())

#Save final dataframe to a new csv file with additional distance column. New file will be named "PatientZipDistances.csv" by default.
df_final.to_csv(r'C:\ZipCodeDistance\zipDistances.csv', sep=',', encoding='utf-8')

#Optional- set parameters for mapping zip codes using folium (leaflet / python spatial mapping package)
locations = df_final[['latitude', 'longitude']]
locationlist = locations.values.tolist()
len(locationlist)
locationlist[7]
print (locationlist)


#set mapping parameters and create map
map = folium.Map(location= site_coords, tiles='CartoDB positron', zoom_start=7)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=df_final['zip'][point]).add_to(map)

#Save map as an html file to the same directory where the source and output csv files are stored.
map.save(r'C:\ZipCodeDistance\AllMap.html')

print('Zip Code calculation and summary script completed successfully.')

#show interactive map if running within notebook or IDE:
map


