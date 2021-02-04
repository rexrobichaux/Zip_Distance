# Zip_Distance
Python 3.x Script for Calculating Geodesic Distances Between a selected lat / lon location and a .csv list of US Zip Codes (centroids).

This Python 3.x script is for parsing csv files (containing a column of zip codes- column must be named 'zip') to 
deterime distances from a set location (Johns Hopkins Center in Baltimore, MD in this example). The output is a new csv file that 
contains a new column (distance_miles) which denotes the distances for all zip codes from the given location, as well as an
interactive map saved to a html file in the same directory where the source and output .csv files exist (C:\ZipCodeDistance by default)
Rex Robichaux, Jan, 2021. rexmrobichaux@gmail.com


# Dependencies:
The ZipCodeDistanceCalculator.py script requires the following Python 3.x Dependencies / Packages to be installed:

pandas

os

numpy

geopy.distance

folium


# Requirements: 
For the script to run, there will need to be a folder named "ZipCodeDistance" created on the local C:\ drive, or the script will need to
be updated to point to the location where the folder has been created (D:\ etc.,). Within the ZipCodeDistance folder, there will need to 
be the Allzipcodes.csv file (can be found within this repository), as well as a file named inputzips.csv. There is a sample inputzips.csv
file within this repository for testing. The inputzips.csv file needs to contain a single column named "zip" which contains the list of 
zip codes that you are interested in determining the distances of from a given location. 

Lastly, the lat /lon parameter for location will need to entered into the ZipCodeDistanceCalculator.py script for the site_coords parameter. 
Standard lat/lon format is required ex(39.301, -76.575). The coordinates will need to be entered again for the distance_miles field calulation line: 
df['distance_miles'] = df.apply(calc_distance, site_coords=(39.301, -76.575).

# Configuration:
Download the following files from this repository: ALlzipcodes.csv, inputzips.csv, ZipCodeDistanceCalculator.py- place them in a folder locally located
as C:\ZipCodeDistance.

Replace the list of zip codes in the inputzips.csv file with the list of zip codes that you would like to find distances to from a given location.

Update the lat / lon parameter in the ZipCodeDistanceCalculator.py python script for the given lat / lon location of interest. 

Execute the script. Once the script completes, there will be two output files in the C:\ZipCodeDistance folder:
1)ZipDistances.csv which is a list of all joined/found US zip codes that were provided in your list, with a distance_miles column showing the geodesic
distance in miles to that zip code (centroid).
2) AllMap.html which is a interactive html file containing a simple folium map with all zip locations plotted as points, centered on the lat / lon
location coordinates that you set in the script. 

