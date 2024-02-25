import random

dice_count = int(input("How many dice do you like to roll? "))

total_sum = 0
for _ in range(dice_count):
    dice_roll = random.randint(4, 8)
    total_sum += dice_roll

print("The sum of the dice rolls is:", total_sum)

