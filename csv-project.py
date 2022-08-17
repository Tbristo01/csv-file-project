import csv

# open csv file 
file = open("example.csv","r")

# read file
rdr = csv.reader(file,delimiter=",")

# output csv content
for row in rdr:
    print(row)

# close file 
file.close()

# open csv file 
file = open("example.csv","a")

newRec=["1005","PAT","Mark","IT"]

# write file
wrt = csv.writer(file)

# write new record into the csv file 
wrt.writerow(newRec)

# close file 
file.close()