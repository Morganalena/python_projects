"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Alena Morgan
email: Alena.karnosova@gmail.com
discord: morganalena
"""
import random
import time

def generate_secret_number():
    # Random 4 unique digits from 1 to 9
    four_numbers = random.sample(range(1, 10), 4)  
    string_digits = []
    
    for digit in four_numbers:
        string_digits.append(str(digit)) 
    
    # Convert the list of digits to a string   
    number_string= ''.join(string_digits) 
    
    return number_string

def guess_number():
    while True:
        guess = input(">>> ")
        
        if validate_guess(guess):
            return guess  # Return the valid guess
        else:
            print(f"Please guess again.",
                  f"\n{'-' * 47}")

def validate_guess(guess):      
    while True:
        try:
            guess_int = int(guess)

            if not guess.isdigit():
                print("Please enter only digits.")
                return False
            
            # Check if it's a 4-digit number
            if len(str(guess)) != 4:
                print("Please enter exactly 4 digits.")
                return False
            
            # Check if the number starts with zero
            if str(guess)[0] == '0':
                print("The number must not start with zero.")
                return False
            
            # Check for duplicate digits
            for d in range(len(str(guess))):
                for e in range(d + 1, len(str(guess))):
                    if str(guess)[d] == str(guess)[e]:
                        print("The number must not contain duplicate digits.")
                        return False

            # If all checks pass, return True
            return str(guess_int)
        
        except ValueError:
            # When input is not an integer
            print("Please enter only digits.")
            return False 

def evaluate_guess(generated_number, guess):
    bulls = 0
    cows = 0 
    
    for i in range(len(generated_number)):
        if generated_number[i] == guess[i]: #Compares digits at identical indexes for matches (bulls)
            bulls += 1
        elif guess[i] in generated_number: 
            cows += 1

    return bulls, cows

def print_result(bulls, cows, num_guesses, start_time):
    if bulls == 4:
        end_time = time.time()
        game_time = end_time - start_time
        print(f"Correct, you've guessed the right number ",
            f"\nin {num_guesses} guess{'es' if num_guesses != 1 else ''}!",
            f"\n{'-' * 47}",
            f"\nThat's {'amazing' if num_guesses <= 6 else 'average' if num_guesses <= 10 else 'not so good'}!"
            f"\nIt took you {game_time:.2f} seconds.")
        return True
    else:
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        return False
    
print(f"Hi there!",
    f"\n{'-' * 47}",  
    f"\nI've generated a random 4-digit number for you.",
    f"\nLet's play a bulls and cows game.",
    f"\n{'-' * 47}",
    f"\nEnter a number:",                
    f"\n{'-' * 47}")
  
generated_number = generate_secret_number()
num_guesses = 0
start_time = time.time()

#Game loop
game_over = False
while not game_over:
    guess = guess_number()  # Get user input for the guess
    num_guesses += 1  # Number of guesses
    bulls, cows = evaluate_guess(generated_number, guess)  
    game_over = print_result(bulls, cows, num_guesses, start_time)
    print('-' * 47)  # Print the separator after each guess

    


