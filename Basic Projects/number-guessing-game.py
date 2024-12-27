## Generatae  a random number
import random
#target_number = random.randint(lower_bound, upper_bound)
 
## set game parameters
lower_bound= 1
upper_bound = 100
max_attempts = 10


target_number = random.randint(lower_bound, upper_bound)
# create  the guessing loop
for attempt in range(max_attempts):
    guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
    if guess<target_number: 
        print("Too low! ")
    elif guess > target_number:
        print("Too High!")
    else:
        print("Congratulations! You guessed the number! ")
        break    