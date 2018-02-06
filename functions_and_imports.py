import import_me
#FUNCTIONS AND IMPORTS (20PTS TOTAL)
# Be sure to comment all your functions as shown in notes

#PROBLEM 1 (how many upper case - 4pts)
# Make a function takes a string as a parameter, then prints how many upper case letters are contained in the string.
# A loop that compares each letter to the .upper() or .lower() of itself will suffice.

def my_function1(word):
    count = 0
    for letter in word:
        if letter == letter.upper():
            count += 1
            if letter == " ":
                count -= 1
    print(count)

my_function1("My name is Grace Philip")


# PROBLEM 2 (Biggest, smallest, average - 4pts)
# Make a function which takes 3 numbers as parameters.
# The function then prints the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.

def my_function2(number_1, number_2, number_3):
    greatest_num = max(number_1, number_2, number_3)
    lowest_num = min(number_1, number_2, number_3)
    average = (number_1 + number_2 + number_3) / 3

    print("Average number is {:.2f}".format(average))
    print("Greatest number is", greatest_num)
    print("Lowest number is", lowest_num)

my_function2 (823, 444, 12)


# PROBLEM 4 (add me, multiply me - 4pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.

def my_function3(number_1, number_2):
    product = number_2 * number_1
    sum = number_2 + number_1
    print("Sum of {} and {} = {}".format(number_1, number_2, sum))
    print("Product of {} and {} = {}".format(number_1, number_2, product))

my_function3 (45, 90)

# PROBLEM 5 (Login - 4pts)
# Make a file called import_me.py in this same project
# Inside this new module/file, make a login function which works according to the flow diagram PasswordFlowchart.png in this folder
# Substitute your name for Rowan's, and use whatever generic password you want.


# PROBLEM 6 (main - 4pts)
# import the file import_me from Problem 5
# Create a main program using the format if __name__ == "__main__": 
# Place every call from problems 1 through 5 into this program.


if __name__ == "__main__":
    import_me.my_function4(name = "Grace")

    # this is the file that you executed/ran


