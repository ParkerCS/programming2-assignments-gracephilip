# Exceptions (no problem set, no lab, no stress)

# Divide by zero error
x = 5

try:
    print(x / 0)
except:
    print("You can't divide by zero!")


# Value error

try:
    x = int("A")
except:
    print("ValueError: we are looking for an integer!")

# File and IOErrors

try:
    my_file = open("my_file.txt", "r")
except:
    print("Problem opening the file.")


# Print out your error (great for debugging)

try:
    5 / 0
except Exception as e:
    print(e)

'''
# MPG calculator
done = False

while not done:
    try:
        miles = float(input("Enter the miles: "))
        gallons = float(input("Enter the gallons: "))
        print(miles / gallons, "MPG")
    except ZeroDivisionError as e:
        print("Enter a non-zero number")
        print(e)
    except ValueError as e:
        print(e)
        print("Enter a real number")
    except:
        print("Unknown error")
        # can also do except exception as e
    finally: # not really useful for us
        print("This always prints when you end")
        done = True
'''
# Built in clean up using WITH

with open("files/nba_scoring_leaders.txt") as f:
    for line in f:
        print(line.strip())

# this automatically closes the file when completed


# HIGH SCORE

my_score = 100

try:
    with open("files/high_score.txt", "r") as f:
        for line in f:
            high_score = int(line.strip())
    if my_score > high_score:
        with open("files/high_score.txt", "w") as f:
            f.write(my_score)
except Exception as e:
    f = open("files/high_score.txt", "w")
    f.write(str(my_score))
    f.close()