import random

class hangmangame:
    def __init__(self, maxwrong = 6, words = "No"):
        if words == "No":
            words = ["PROGRAMMING", "PHILOSOPHY", "LANGUAGE", "HANGMAN", "ENGINEER", "LABORATORY", "ELECTRONIC", "COMPUTER", "SOFTWARE", "DATABASE"]
        
        self.words = words
        self.maxwrong = maxwrong
        self.reset()

    def reset(self):
        self.selected = self.chooseRan()
        self.hidden = ['_'] * len(self.selected)
        self.guessed = []
        self.wrongGuess = 0

    def chooseRan(self):
        return random.choice(self.words).upper()

    def display(self):
        print(' '.join(self.hidden))

    # def get_guess(self):
    #     while self.wrongGuess < self.maxwrong and '_' in self.hidden:
    #         guess = input("Guess a letter: ").upper()
    #         if len(guess) == 1 and guess.isalpha():
    #             if guess not in self.guessed:
    #                 self.guessed.append(guess) 
    #                 return guess
    #             else:
    #                 print("You already guessed that letter.")
    #                 self.wrongGuess += 1
    #         else:
    #             print("Invalid input. Please enter a single alphabet.")

    #         self.display()
    #         self.hangman()
    #         print(f"Incorrect guesses: {self.wrongGuess}")

    def updateHidden(self, guess):
        for i, letter in enumerate(self.selected):
            if letter == guess:
                self.hidden[i] = guess

    def hangman(self):
        stages = [
            """
---------
                    
            """,
            """
---------
        O
            """,
            """
---------
        O
       /
            """,
            """
---------
        O
       / \\
            """,
            """
 ---------
         O
        /|\\
            """,
            """
---------
        O
       /|\\
        |
       /
            """,
            """
---------
        O
       /|\\
        |
       / \\
            """
        ]
        # Ensure the index is within the valid range
        stage_index = min(self.wrongGuess, len(stages) - 1)
        print(stages[stage_index])

    def play(self):
        print("Welcome to Hangman!")
        print(f"The word has {len(self.selected)} letters.")
        self.display()

        while self.wrongGuess < self.maxwrong and '_' in self.hidden:
            guess = input("Guess a letter: ").upper()
        
            if len(guess) == 1 and guess.isalpha():
                if guess not in self.guessed:
                    self.guessed.append(guess)
                    if guess in self.selected:
                        self.updateHidden(guess)
                    else:
                        self.wrongGuess += 1
                else:
                    print("You already guessed that letter.")
                    self.wrongGuess += 1
            else:
               print("Invalid input. Please enter a single alphabet.")
    
            # Display the updated state of the game
            self.display()
            self.hangman()
            print(f"Incorrect guesses: {self.wrongGuess}")
            
        if '_' not in self.hidden:
            print("Congratulations! You guessed the word correctly!")
        else:
            print(f"Sorry, you lost! The word was: {self.selected}")
