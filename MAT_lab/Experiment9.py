# WAP to read and write the customized data into .xlsx file/.csv file in python.

# # -------------csv file-------------
# import pandas as pd
# # read a csv file
# df = pd.read_csv(input("Enter the path of the file"))

# write a csv file
import csv  
    
# field names  
fields = ['Name', 'Branch', 'Year', 'CGPA']  
    
# data rows of csv file  
rows = [ ['Kunal', 'CSE', '2nd','7.8'],
['Sushant','CSE','2nd','8.1']]  
    
# name of csv file  
filename = "student_data.csv"
    
 
with open(filename, 'w') as csvfile:  
   csvwriter = csv.writer(csvfile)  
   csvwriter.writerow(fields)  
   csvwriter.writerows(rows) 


# ------------------------------Excel file ------------------------------
# read the excel file
# write the excel file
