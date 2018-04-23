from gmplot import *
import csv
import random

# In 2013, an interesting dataset was released for Chicago which identified a number of food deserts.
# In many areas of the city, there were no suitable grocery stores with adequate produce, meats, refrigerated, and frozen food sections
# Many areas were only served by corner stores and convenience stores.

# Using gmplot and the chicago grocery csv, which contains updated grocery store data, 
# create a map with the following characteristics.
# - Map is centered on Chicago at a zoom level that shows all stores (5pts)
# - All adequate grocery stores are plotted (could be scatterplot, circles, or markers) (use the one looks best to you) (10pts)
#   Inadequate grocery stores are NOT plotted (you decide what inadequate means)
# - Shows a heatmap which helps to visualize the greatest concentration of adequate stores. (10pts) 
#   Your heatmap should be optimized for the city level view.  Tweak the radius and maxIntensity to adjust blob.


# Challenges:  
# Instead of a heatmap, make each store a circle with varying size based on square footage of the store.  
# Filter out all liquor stores, drug stores, and convenience stores.
# Place markers or other indicators where you still see inadequate food access.

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"



with open("files/Grocery_Stores_-_2013.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data.pop(0))

lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]
size = [random.randrange(1, 500) for x in data]

mymap = GoogleMapPlotter(41.876448, -87.629539, 10, apikey=apikey)  # lat, long, zoom_level, apikey=var


mymap.scatter(lats, longs, marker=False, color="red", size=10, alpha=0.5)

for i in range(len(lats)):
    mymap.circle(lats[i], longs[i], size[i])


store_names = ["LIQUOR STORE", "DRY STORE", "GROCERY STORE", "WALGREENS"]

index = 0
while index < len(store_names):
    if "LIQUOR" in store_names[index] or "WALGREENS" in store_names[index]:
        del store_names[index]
    index += 1
print(store_names)

mymap.draw('grocery.html')
