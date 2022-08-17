import csv

# open csv file 
file = open("example.csv","r")

# read file
rdr = csv.reader(file,delimiter=",")

# output csv content
for row in rdr:
    if row[3]=="IT":
        print(row)

# close file 
file.close()
