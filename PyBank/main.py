# Modules
import os
import csv
#set the variables
row_num = 0
totalMonths = 0
totalRevenue = 0
previousRevenue = 0
revenue_change = 0
revenue_change_list= []
Date = []
# Set path for file
budget_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Resources", "Financial Analysis")
# Open and read csv
with open(budget_path, newline="") as csvfile:
     budget_reader = csv.reader(csvfile, delimiter=",")
     
# Read the header row first (skip this part if there is no header)
     csv_header = next(csvfile)
     print(f"Header: {csv_header}")    

#To loop through the data to collect the answers
     for row in budget_reader:
          
        # Totaling
         totalMonths = totalMonths + 1
         totalRevenue = totalRevenue + int(row[1])
         
        #changes of revenue calculations
         revenue_change = int(row[1]) - previousRevenue 
         previousRevenue = int(row[1]) 
        
         #add changes in new list
         revenue_change_list.append(revenue_change)
         Date.append(row[0])
     revenue_change_list.remove(revenue_change_list[0])
     
# Calculate the average change in revenue
     totalChange = (sum(revenue_change_list))
     AvgRevenueChange = round(totalChange /len(revenue_change_list),2)
     
# Calculate the greatest increment and greatest decrement in revenue     
     greatest_increase_rev = max(revenue_change_list)
     greatest_decrease_rev = min(revenue_change_list)

 # Calculate Date of increment and decrement    
     increase_index= revenue_change_list.index(greatest_increase_rev)
     greatestRevIncrementDate = Date[increase_index]
     
     decrease_index = revenue_change_list.index(greatest_decrease_rev)
     greatestRevDecrementDate = Date[decrease_index]
# print results to Terminal
     print("---------------------------------------------------------------")
     print("Financial Analysis")
     print("---------------------------------------------------------------")
     print(f"Total Months: {totalMonths}")
     print(f"Total : {totalRevenue}")
     print(f"Average  Change: ${AvgRevenueChange}")
     print( f"Greatest Increase in Profits: {greatestRevIncrementDate}(${greatest_increase_rev})")
     print( f"Greatest Decrease in Profits: {greatestRevDecrementDate}(${greatest_decrease_rev})")

#To export a text file with the results
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as textfile:
    # Initialize csv.writer
     csvwriter = csv.writer(csvfile, delimiter=',')

  #print results to Text file
     textfile.write("Financial Analysis\n")
     textfile.write("-------------------------------------------------------------\n")
     textfile.write(f"Total Months: {totalMonths}\n")
     textfile.write(f"Total : {totalRevenue}\n")
     textfile.write(f"Average  Change: ${AvgRevenueChange}\n")
     textfile.write(f"Greatest Increase in Profits: {greatestRevIncrementDate}(${greatest_increase_rev})\n")
     textfile.write(f"Greatest Decrease in Profits: {greatestRevDecrementDate}(${greatest_decrease_rev})\n")
       
        