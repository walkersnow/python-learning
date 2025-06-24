# hari_ke_48.py
import csv

data = [["Nama", "Umur"], ["Dika", 20], ["Ical", 21]]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
