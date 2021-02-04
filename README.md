# Zip_Distance
Python 3.x Script for Calculating Geodesic Distances Between a Location and a .csv list of US Zip Codes (centroids).

This Python 3.x script is for parsing csv files (containing a column of zip codes- column must be named 'zip') to 
deterime distances from a set location (Johns Hopkins Center in Baltimore, MD in this example). The output is a new csv file that 
contains a new column (distance_miles) which denotes the distances for all zip codes from the given location, as well as an
interactive map saved to a html file in the same directory where the source and output .csv files exist (C:\ZipCodeDistance by default)
Rex Robichaux, Jan, 2021. rexmrobichaux@gmail.com


# Dependencies:
The ZipCodeDistanceCalculator.py script requires the following Python 3.x Dependencies / Packages to be installed:
-pandas
-os
-numpy
-geopy.distance
-folium

# Requirements: 
For the script to run, there will need to be a folder named "ZipCodeDistance" created on the local C:\ drive, or the script will need to
be updated to point to the location where the folder has been created (D:\ etc.,). Within the ZipCodeDistance folder, there will need to 
be the Allzipcodes.csv file (can be found within this repository), as well as the inputzips.csv file. The inputzips.csv file needs to
contain a single column named "zip" which contains the list of zip codes that you are interested in determining the distances of from a
given location. 

Lastly, the parameter for location will need to entered into the ZipCodeDistanceCalculator.py script for the site_coords parameter. Standard
lat/lon format is required ex(39.301, -76.575).

