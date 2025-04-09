import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 5

print("🎮 Welcome! Guess the number between 1 and 10. You have 5 tries.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("🎉 You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    if attempts == max_attempts:
        print(f"❌ Sorry! You've used all {max_attempts} tries. The number was {secret_number}.")
