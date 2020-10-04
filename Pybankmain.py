
#Import file paths across operating systems/ Module for reading CSV files

import os
import csv

#Set the Path
csvpath=os.path.join('Resources', "budget_data.csv")

#Create the Lists to store Data
Month = []
Revenue = []
Date = []
Revenue_Changes = []
Greatest_Increase_Profits=["",0]
Greatest_Decrease_Profits=["",999999999999999]

#Define Variables
Month_count = 0
Total_revenue= 0
Total_change_revenue= 0
outputfile= os.path.join('Analysis', "Budget_Data.txt")


#Open the CSV
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #SkipHeader/FirstRow
    csv_header = next(csvreader)
    firstrow=next(csvreader)
    Month_count+=1
    Total_revenue+=int(firstrow[1])
    prev_revenue=int(firstrow[1])
    
    # Read each row of data after the header
    for row in csvreader:
        
        #Totaling Months
        Month_count += 1
      

        #Totaling Revenue
        Total_revenue += int(row[1])

        #Track the revenue change
        Total_change_revenue= int(row[1])-prev_revenue
        prev_revenue=int(row[1])
        Revenue_Changes.append(Total_change_revenue)
        Date.append(row[0])

        #CalculateGreatestIncrease
        if Total_change_revenue > Greatest_Increase_Profits[1]:
            Greatest_Increase_Profits[0]=row[0]
            Greatest_Increase_Profits[1]=Total_change_revenue
        
        #CalculateGreatestDecrease
        if Total_change_revenue < Greatest_Decrease_Profits[1]:
            Greatest_Decrease_Profits[0]=row[0]
            Greatest_Decrease_Profits[1]=Total_change_revenue


# Calculate the Average Revenue Change
revenue_avg = sum(Revenue_Changes) / len(Revenue_Changes)


print(revenue_avg)
#Printoutputs
output=(
  f"Financial Analysis\n"
  f"----------------------------\n"
  f"Total Months : {Month_count}\n"
  f"Total: ${Total_revenue}\n"
  f"Average  Change: ${revenue_avg}\n"
  f"Greatest Increase in Profits:${Greatest_Increase_Profits}\n" 
  f"Greatest Decrease in Profits:${Greatest_Decrease_Profits}\n" 
  
)
print(output)


with open(outputfile, "w") as txt_file:
    txt_file.write(output)




