import csv
import matplotlib.pyplot as plt


# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors (15pts)
# open and read in the "Libraries_-_2018_Visitors_by_Location.csv" file into a list (use file located in the file folder, read in using csv library).
# calculate (and make a list of) the total visitors to Chicago libraries each month.  
# Do not plot every library individually.  Instead, find the total for all libraries each month and plot that.
# Make a BAR GRAPH with the total visitors on the y and month on the x.  
# label the x with the month.  Rotate the text so we can read it.  (see example problem).  Use the tight_fit command to show all text.
# label axes, title the graph as necessary.


with open("files/Libraries_-_2017_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)  # make a reader object
    data = list(reader)  # casting the reader object as a list

total_visitors = []

month_names = data.pop(0)[1:-1]

for i in range(1, 13):
    visitors = [x[i] for x in data][1:-1]
    visitors = [int(x) for x in visitors]
    total_visitors.append(sum(visitors))

print(total_visitors)

months = [x for x in range(1, 13)]

plt.figure(1, figsize=(10, 6), tight_layout=True, facecolor="lightblue")
plt.bar(months, total_visitors, color="blue")
plt.xticks(months, month_names, rotation=90, fontsize=8)
plt.title("Total Monthly Visitors - 2017", fontsize=25)
plt.ylabel("Number of Visitors")
plt.show()


# MATPLOTLIB PROBLEM # 2 
# Chicago Public Transit Usership Graph (20pts)
# go to https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
# download the CTA ridership data as a csv.
# Read the data into a list using the csv library.
# Make a plot of paratransit, bus, rail, and total numbers by year (all on the same graph).
# Make each line, points, and color different for the four graphs.
# Make a legend to identify each line.
# Label axes and give your graph a title.  Change it in any other way you see necessary to give it a clean look.

with open("files/CTA_-_Ridership_-_Annual_Boarding_Totals.csv") as f:
    reader = csv.reader(f)  # make a reader object
    data = list(reader)  # casting the reader object as a list


total_num = []

cta_names = data.pop(0)[1:-1]

for i in range(1, 6):
    visitors = [x[i] for x in data][1:-1]
    visitors = [int(x) for x in visitors]
    total_num.append(sum(visitors))

year_num = [x[0] for x in data]

for line in data:
    total_by_year = [x[i] for x in data]




print(total_num)

months = [x for x in range(1, 13)]
