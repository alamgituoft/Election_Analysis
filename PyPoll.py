#review data
#the total no of votes cast
#complete list of candidates who received votes
#% of votes each candidate won
#total no. of votes each candidate won
#winner of election based on popular vote 

#Add dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign variable to save file to path 
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)









