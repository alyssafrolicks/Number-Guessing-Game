import random

def get_random_num():
    num = random.randint(1, 100)
    return num
    
def level(answer, chances):
    print("Let's start the game!")
    count_of_guesses = 1
    while count_of_guesses <= chances:
        print("Enter your guess: ")
        num = int(input())
        status = check_guess(num, answer)
        if status[0] == True:
            print(f"Congratulations! You guessed the correct number in {count_of_guesses} attempts.")
            break
        elif status[0] == False:
            if status[1] == "invalid":  # right now it will not count invalid input as a guess, but it will still print the message and ask for input again
                continue
            elif status[1] == "less":
                print(f"Incorrect! The number is less than {num}.")
            elif status[1] == "greater":
                print(f"Incorrect! The number is greater than {num}.")
            else:
                print("Something went wrong. Please try again.")
        count_of_guesses += 1
    print("Game Over! You are out of guesses. The correct number was:", answer) 
    print("Do you want to play again? (yes/no)")
    play = input().lower()
    if play == "yes":
        main()
    else:
        print("Thank you for playing! Goodbye!")
    
    
    
def check_guess(guess, num):
    if guess < 1 or guess > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        return False, "invalid"
    if guess == num:
        return True, "equal"
    elif num < guess:
        return False, "less"
    elif num > guess:
        return False, "greater"
    else:
        print("Something went wrong//Invalid input. Please enter a number between 1 and 100.")
    
def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")
    number = get_random_num()
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    print("Enter your choice:")
    choice = int(input())
    if choice == 1:
        print("You have selected Easy difficulty level. You have 10 chances to guess the number.")
        level(number, 10)
    elif choice == 2:
        print("You have selected Medium difficulty level. You have 5 chances to guess the number.")
        level(number, 5)       
    elif choice == 3:
        print("You have selected Hard difficulty level. You have 3 chances to guess the number.")
        level(number, 3)
    else:
        print("Invalid choice. Please select a valid difficulty level.")
        main() # runs again?

if __name__ == "__main__":
    main()
    #print(check_guess(50, 50))
    #print(check_guess(50, 75))
    #print(check_guess(75, 50))
    #level(50, 5)
    
    