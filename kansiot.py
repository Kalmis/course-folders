# -*- coding: utf-8 -*-
import os
import time
import math
from time import mktime
from datetime import date

# Example
# MyCoursesista kopioitu kurssikoodi, nimi sekä päivämäärät:
# ELEC-C5340 - Sovellettu digitaalinen signaalinkäsittely, 07.09.2015-09.12.2015
# Kurssista saatavat nopat:
# 5

# Read information
info = input("MyCoursesista kopioitu kurssikoodi, nimi sekä päivämäärät:").split(" ")
op = int(input("Kurssista saatavat nopat:"))

# Take course code from the info string
code = info[0]

# Take dates from string, parse to time_sturcture, convert to date and calculate weeks
# between dates
dates = info[-1].split("-")
startdate = time.strptime(dates[0], "%d.%m.%Y")
startdate = date.fromtimestamp(mktime(startdate))
enddate = time.strptime(dates[1], "%d.%m.%Y")
enddate = date.fromtimestamp(mktime(enddate))
weeks = math.ceil(((enddate-startdate).days)/7)

# Remove course code, "-", dates and "," from the info list
del info[0:2]
del info[-1]
info[-1] = info[-1][0:-1]

# Make one string from info list, put " " between words
info = ' '.join(info)
# Make directory name
directory = info + " (" + str(op) + " op) " + code

# Make the directory and subdirectories
print("Creating main directory: ", directory)
os.makedirs(directory)
print("Creating subdirectory: ", directory, "/Esimerkki tehtavat")
os.makedirs(directory + "/Esimerkki tehtavat")
print("Creating subdirectory: ", directory, "/Muu materiaali")
os.makedirs(directory + "/Muu materiaali")
print("Creating subdirectory: ", directory, "/Tehtavat")
os.makedirs(directory + "/Tehtavat")
print("Creating subdirectory: ", directory, "/Vanhat tentit")
os.makedirs(directory + "/Vanhat tentit")
print("Creating subdirectory: ", directory, "/Yleista")
os.makedirs(directory + "/Yleista")
# Make so many "Viikko x" subdirectories as there is weeks in the course
for i in range(1, weeks+1):
    print("Creating subdirectory: ", directory, "/Viikko ", str(i))
    os.makedirs(directory + "/Viikko " + str(i))
print("All done!")
