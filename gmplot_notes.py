from gmplot import *
import csv

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"

mymap = GoogleMapPlotter(41.923079, -87.638230, 14, apikey=apikey)  # lat, long, zoom_level, apikey=var

mymap.marker(41.923079, -87.638230) # lat, long

mymap.circle(41.933079, -87.638230, 500, "#FF0000", ew=3) # lat, long, radius(m), web_color, edge_width=int

my_lats = [41.923079 + x/50 for x in range(10)]
my_longs = [-87.638230 + x/50 for x in range(10)]

mymap.plot(my_lats, my_longs, "blue")

my_lats = [41.923079, 41.933079, 41.923079]
my_longs = [-87.638230, -87.648230, -87.658230]
mymap.polygon(my_lats, my_longs, fc="yellow", ew=5, ec="red") #lats, longs, color, face color, edge width, edge color

with open("../files/Parks_-_Public_Art.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data[0])



mymap.draw('mymap.html')