# hari_ke_47.py
import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
