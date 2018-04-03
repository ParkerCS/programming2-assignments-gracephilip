# Sorting
import random
import time
# Swap Values


a = 1
b = 2
print(a, b)


temp = a # creates a temporary variable
a = b
b = temp
print(a, b)


a, b = b, a  # pythonic way
print(a, b)


# Random list of 100 number (1, 99)
rando_list = []
rando_list = [random.randrange(1, 100) for x in range(100)]
print(rando_list)


def selection_sort(rando_list):
    for cur_pos in range(len(rando_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(rando_list)):
            if rando_list[scan_pos] < rando_list[min_pos]:
                min_pos = scan_pos
        rando_list[cur_pos], rando_list[min_pos] = rando_list[min_pos], rando_list[cur_pos]
    return rando_list


my_sorted_list = selection_sort(rando_list)


selection_sort(rando_list)
print(rando_list)


# Insertion sort
rando2 = [random.randrange(1, 100) for x in range(100)]
print(rando2)


for key_pos in range(1, len(rando2)):
    key_value = rando2[key_pos]
    scan_pos = key_pos - 1  # look to the dancer on the left
    while (scan_pos >= 0) and (rando2[scan_pos] > key_value):
        rando2[scan_pos + 1] = rando2[scan_pos]
        scan_pos -= 1

    # now everything is shifted to make room for the key_value
    rando2[scan_pos + 1] = key_value


print(rando2)

start_time = (time.perf_counter())
sort_me = [random.random() for x in range(100)]
selection_sort(sort_me)
print(time.perf_counter() - start_time)

sort_me = [random.random() for x in range(1000)]
start_time = (time.perf_counter())
sort_me.sort(reverse = True)
print(time.perf_counter() - start_time)

my_names = ["Abe", "deb", "Eve", "Rob", "bob", "Zed", "Nan"]
my_names.sort(reverse=True, key=str.upper)
print(my_names)



my_list1 = [3, 5, 1, 8, 5, 3]
my_list2 = [[8, 2], [5, 1], [6, 3]]

my_list1.sort() # sorts in place
my_list1 = sorted(my_list1) # equivalent function that RETURNS
print(my_list1)

my_list2.sort()
print(my_list2)

# lambda function - anonymous sing line function
# lambda parameters: what to return

double = lambda x: 2 * x
print(double(10))

products = lambda x, y: x * y
print(products(9, 8))

my_list2.sort(key=lambda x: x[1])
print(my_list2)

my_list3 = ["Bev", "Cam", "Abe", "ava"]
my_list3.sort(key=lambda x: x.upper())
print(my_list3)