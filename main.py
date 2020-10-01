#Python HW

#Import file paths across operating systems/ Module for reading CSV files

import os
import csv

#Set the Path
csvpath=os.path.join('Resources', "budget_data.csv")

#Create the Lists to store Data
Month = []
Revenue = []
Date = []


#Define Variables
Month_count = 0
Total_revenue= 0
Total_change_revenvue= 0
Initial_revenue = 0 
prev_revenue = 0



#Open the CSV
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #SkipHeader
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        #Totaling Months
        Month_count += 1

        #Totaling Revenue
        Total_revenue += int(row[1])

        #Track the revenue change
        Total_change_revenvue= int(row[1])-prev_revenue
        prev_revenue=int(row[1])
        




        






#print the outcomes
        



