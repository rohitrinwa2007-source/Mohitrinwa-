import random

class GuessTheNumber:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.guesses = 0
        self.score = 100

    def make_guess(self, guess):
        self.guesses += 1
        if guess < self.target_number:
            self.score -= 1
            return "Higher! Try again."
        elif guess > self.target_number:
            self.score -= 1
            return "Lower! Try again."
        else:
            return f"Congratulations! You've guessed the number {self.target_number} in {self.guesses} attempts with a score of {self.score}."

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.guesses = 0
        self.score = 100
        return "Game reset! New number generated."

if __name__ == '__main__':
    game = GuessTheNumber()
    print("Welcome to the Guess The Number Game!")
    while True:
        guess = int(input("Enter your guess (1-100): "))
        result = game.make_guess(guess)
        print(result)
        if guess == game.target_number:
            break
        
    print("Thanks for playing!")