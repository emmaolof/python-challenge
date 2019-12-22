# Dependencies
import csv

# Files to Load
csvpath= ('budget_data.csv')

# Set the average
def avg(nums):
        total=0
        for num in nums:
            total+=num
        return round(total/len(nums),2)

        # Read Files    
with open(csvpath,'r',newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csvheader=next(csvreader)

# assign a change list, and define variables
    changes=[]
    totalamount=0
    totalmonths=0
    change_max=0
    change_min=0
    change_max_month=''
    change_min_month=''
    initialpl=0
    initialmonth=''
    for row in csvreader:
        if initialmonth !='':
            change=int(row[1])-initialpl
            changes.append(change)
            if change>change_max:
                change_max=change
                change_max_month=row[0]
            if change<change_min:
                change_min=change
                change_min_month=row[0]
        initialpl=int(row[1])
        initialmonth=row[0]
        totalamount+=int(row[1])
        totalmonths+=1
    avgchange=avg(changes)

# print analysis 
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${totalamount}")
    print(f"Average Change :${avgchange}")
    print(f"Greatest Increase in Profits: ${change_max} in {change_max_month}")
    print(f"Greatest Decrease in Profits: ${change_min} in {change_min_month}")

# Output Files
    with open('budget_analysis.txt', 'w', newline='') as file:
        file.write("Financial Analysis\n")
        file.write("-------------------------\n")

        file.write("Total Months: " + str(totalmonths)+"\n")
        file.write("Total: $" + str(totalamount)+"\n")
        file.write("Average Change: $" + str(avgchange)+"\n")
        file.write("Greatest Increase in Profits: $" + str(change_max) + " in " + change_max_month + "\n")
        file.write("Greatest Decrease in Profits: $" + str(change_min) + " in " + change_min_month + "\n")