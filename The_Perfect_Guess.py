import random
import time

print("Welcome to the Perfect Guess Game!")

while True:
    level = input("Choose difficulty (easy, medium, hard): ").lower()
    if level == "easy":
        randomNum = random.randint(1, 10)
    elif level == "medium":
        randomNum = random.randint(1, 50)
    elif level == "hard":
        randomNum = random.randint(1, 100)
    else:
        print("Invalid choice. Defaulting to easy mode.")
        randomNum = random.randint(1, 10)

    guessNumber = -1
    guesses = 0
    time_limit = 30  # seconds
    start_time = time.time()

    while guessNumber != randomNum:
        # Check if time has run out
        if time.time() - start_time > time_limit:
            print("\n⏰ Time's up! You didn't guess in time.")
            break

        try:
            guessNumber = int(input("Guess the number: "))
            guesses += 1
            if guessNumber > randomNum:
                print("Lower number please")
            elif guessNumber < randomNum:
                print("Higher number please")
        except ValueError:
            print("Please enter a valid number!")

    else:
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print(f"\n🎉 You guessed the number {randomNum} correctly in {guesses} attempts.")
        print(f"⏱️ Time taken: {total_time} seconds")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break