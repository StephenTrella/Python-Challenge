#Import file paths across operating systems/ Module for reading CSV files

import os
import csv

#Set the Path
csvpath=os.path.join('Resources', "election_data.csv")

#Create the Lists/Variables to store Data
Candidates_Dict = {}
Total_votes = 0
vote_counts = []
outputfile= os.path.join('Analysis', "Election_Data.txt")
total_candidates= 0
Winner = ""
Max_Votes=0


#Open the CSV
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')


    #Skip Header 
    csv_header = next(csvreader)


    # Read each row of data after the header
    for row in csvreader:

        #Totaling Votes
        Total_votes += 1
        
     
        #List of candidates who received votes/Candidate Count
        candidate =(row[2])
        if candidate in Candidates_Dict:
            Candidates_Dict[candidate]+=1
        else:
            Candidates_Dict[candidate]=1

#Printoutputs
with open(outputfile, "w") as txt_file:
    

    output=(
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes : {Total_votes}\n"
        f"-------------------------\n"
    )
    txt_file.write(output)
    #Calculate Percentage
    for key, value in Candidates_Dict.items():  
            vote_percentage = round((value /Total_votes) * 100,3) 
            print(f"{key}: {vote_percentage}% ({value})")
            txt_file.write(f"{key}: {vote_percentage}% ({value})\n")
            #Find Winner
            if value > Max_Votes :
                Max_Votes=value
                Winner=key

    print(f"-------------------------")
    txt_file.write("-------------------\n")
    
    print(f"Winner :{Winner}")
    txt_file.write(f"Winner :{Winner}\n")
    
    