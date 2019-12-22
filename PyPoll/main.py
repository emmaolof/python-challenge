# Dependencies
import csv

# Files to Load
csvpath= ('election_data.csv')
 
 # Read Files
with open(csvpath,'r',newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csvheader=next(csvreader)

# assign lists, and define variables
    candidates=[]
    totalvotes=0
    correy=[]
    khan=[]
    li=[]
    tooley=[]
    correyvote=0
    khanvote=0
    livote=0
    tooleyvote=0

    #Loop through all the rows of data we collect
    for e in csvreader:
        if e[2]=='Correy':
            correyvote+=1
            correy.append(correyvote)
        elif e[2]=='Khan':
            khanvote+=1
            khan.append(khanvote)
        elif e[2]=='Li':
            livote+=1
            li.append(livote)
        elif e[2]=="O'Tooley":
            tooleyvote+=1
            tooley.append(tooleyvote)
        totalvotes+=1
    correyrate=round((len(correy)/totalvotes)*100,3)
    khanrate=round((len(khan)/totalvotes)*100,3)
    lirate=round((len(li)/totalvotes)*100,3)
    tooleyrate=round((len(tooley)/totalvotes)*100,3)
    voterate=[correyrate, khanrate, lirate , tooleyrate ]
    winner=max(voterate)

#print out the results
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {totalvotes}") 
    print("-----------------------------")   
    print(f"Khan: {khanrate}% ({khanvote})")
    print(f"Correy: {correyrate}% ({correyvote})")
    print(f"Li: {lirate}% ({livote})")
    print(f"O'Tooley: {tooleyrate}% ({tooleyvote})")
    print("-----------------------------")
    print("Winner: Khan")
    print("-----------------------------")

## Output Files
    with open('electionresults.txt', 'w', newline='') as file:
        file.write("Election Results\n")
        file.write("-----------------------------\n")
        file.write(f"Total Votes: {totalvotes}\n")
        file.write("-----------------------------\n")
        file.write(f"Khan: {khanrate}% ({khanvote})\n")
        file.write(f"Correy: {correyrate}% ({correyvote})\n")
        file.write(f"Li: {lirate}% ({livote})\n")
        file.write(f"O'Tooley: {tooleyrate}% ({tooleyvote})\n")
        file.write("-----------------------------\n")
        file.write("Winner: Khan")
        file.write("-----------------------------\n")