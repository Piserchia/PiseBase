import csv
import sys
import time 


with open('oct2019testdata.txt') as csvfile:
    readCSV = csv.reader(csvfile, ",")
    for row in readCSV:
            print(row)
            print(row[0])
            print(row[0], row[1], row[2])
    