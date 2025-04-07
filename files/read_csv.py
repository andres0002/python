import csv

with open("files\\file.csv") as file:
    print("Ok...")
    
    # leer file.
    for row in csv.reader(file):
        print(row)