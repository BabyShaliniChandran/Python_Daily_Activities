'''
#reading the csv file
import csv
with open("data.csv",newline='') as f:
	reader=csv.reader(f)#creates a reader object
	for row in reader:
		print(row)

#the next gentrator skip the row
import csv
with open("data.csv",newline='') as f:
	reader=csv.reader(f)#creates a reader object
	next(reader)
	for row in reader:
		print(row)

#converthing the list as csv
import csv 
with open("data.csv",newline='') as f:
	reader=csv.reader(f)
	data=list(reader)
print(data)

#prints the lines 
import csv
with open("data.csv",newline='') as f:
	reader=csv.reader(f)#creates a reader object
	for row in reader:
		print(reader.line_num,row)

import csv
with open("data.csv") as f:
	reader=csv.DictReader(f)
	for row in reader:
		print(row["Name"],row["Age"])

'''





















