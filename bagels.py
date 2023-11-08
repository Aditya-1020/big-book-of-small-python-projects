import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f"I am Thinking of a {NUM_DIGITS} digit number with no repeated digits.\nTry to guess what it is. Here are some clues-\n"
          "When is say:         That means:\n"
          "Pico                 One digit is correct but in the wrong position\n"
          "Fermi                One digit is correct and in the right position\n"
          "Bagels               No digits is correct.\n"
          
          "For example if the number was 248 and your guess was 843, the\n"
          "clues would be Fermi Pico.")
    
    while True:
        number_to_guess = getSecretNum()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} guesses to get it right")
        
        NUM_GUESSES = 1
        
        while NUM_GUESSES <= MAX_GUESSES:
            guess = input(f"Guess #{NUM_GUESSES}: ")
            
            if len(guess) != NUM_DIGITS or not guess.isdigit():
                print(f"Invalid input. Please enter a {NUM_DIGITS}-digit number.")
                continue
            
            NUM_GUESSES += 1
            clues = getClues(guess, number_to_guess)
            
            for clue in clues:
                print(clue)
                
            if guess == number_to_guess:
                print("COngratulations! You have guessed correct")
        
        else:
            print(f"Out of guesses. The secret number was {number_to_guess}.")
        
        play_again = input("Do you want to play again? (yes or no): ")
        if play_again.lower() != "yes":
            break
        
def getSecretNum():
    num = str(random.randint(100,999))
    while len(str(num)) < NUM_DIGITS:
        num = str(random.randint(100,999))
    return num

def getClues(guess, secret):
    clues = []
    for i in range(NUM_DIGITS):
        if guess[i] == secret[i]:
            clues.append("Fermi")
        elif guess[i] in secret:
            clues.append("Pico")
    if not clues:
        clues.append("Bagels")
    return clues

main()