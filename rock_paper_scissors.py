import random

def play_game():
    """Rock, Paper, Scissors Game"""
    
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0
    
    print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
    print("=" * 40)
    print("Type 'quit' to exit the game")
    print("=" * 40)
    
    while True:
        print(f"\n📊 Score - You: {player_score} | Computer: {computer_score}")
        
        player_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
        
        if player_choice == 'quit':
            print(f"\n🏁 Final Score - You: {player_score} | Computer: {computer_score}")
            if player_score > computer_score:
                print("🎉 You won the game!")
            elif player_score < computer_score:
                print("😢 Computer won the game!")
            else:
                print("🤝 It's a tie!")
            break
        
        if player_choice not in choices:
            print("❌ Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f"\n👤 You chose: {player_choice.upper()}")
        print(f"🤖 Computer chose: {computer_choice.upper()}")
        
        if player_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("✅ You win this round!")
            player_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

if __name__ == "__main__":
    play_game()