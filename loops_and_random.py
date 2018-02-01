# LOOPS (16pts TOTAL)
import random
# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

fib_1 = 1
fib_0 = 1
fib_2 = 2

print(fib_0)
print(fib_1)
for i in range(0, 1000):
    fib_2 = fib_0 + fib_1
    fib_0 = fib_1
    fib_1 = fib_2
    print(fib_2)
    if fib_2 > 1000:
        break

# PROBLEM 2 (Dice Sequence - 6pts)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

for i in range(100000):
    first_dice = random.randrange(1, 7)
    second_dice = random.randrange(1, 7)
    third_dice = random.randrange(1, 7)
    fourth_dice = random.randrange(1, 7)
    fifth_dice = random.randrange(1, 7)
    if fifth_dice > fourth_dice:
        continue
        if fourth_dice > third_dice:
            continue
            if third_dice > second_dice:
                continue
                if second_dice > first_dice:
                    continue
    else:
        break
print(first_dice, "\t", second_dice, "\t", third_dice, "\t", fourth_dice, "\t", fifth_dice)

# I did it twice two different ways
# The second one works better but prints things oddly
trials = 100000
win = 0
for i in range(trials):
    roll_count = 0
    roll = random.randrange(1, 7)
    for j in range(4):
        new_roll = random.randrange(1,7)
        #print(roll, new_roll)
        if new_roll < roll:
            #print("lose")
            break
        else:
            roll = new_roll
            roll_count += 1
        if roll_count == 4:
            #print("win")
            win += 1
win_percent = (win / trials) * 100
print(win_percent)









# PROBLEM 3 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve. 

for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(1, 10):
                num1 = (int(str(a) + str(b) + str(c) + str(d))) * 4
                num2 = int(str(d) +str(c) +str(b) + str(a))
                if num1 == num2:
                    print(num1 / 4)
