import random

def play_game(difficulty):
    """Play a single round of the guessing game."""
    if difficulty == 1:
        max_num = 10
        max_attempts = 5
    elif difficulty == 2:
        max_num = 50
        max_attempts = 8
    else:  # difficulty == 3
        max_num = 100
        max_attempts = 10
    
    secret = random.randint(1, max_num)
    attempts = 0
    
    print(f"\n🎮 Difficulty: {'Easy' if difficulty == 1 else 'Medium' if difficulty == 2 else 'Hard'}")
    print(f"I'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it!\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between 1 and {max_num}: "))
            
            # Validate input
            if guess < 1 or guess > max_num:
                print(f"⚠️  Please enter a number between 1 and {max_num}.")
                continue
            
            attempts += 1
            
            if guess == secret:
                print(f"\n🎉 Congratulations! You guessed correctly in {attempts} attempt(s)!")
                return True
            elif guess < secret:
                print(f"📉 Too low. Try again. ({max_attempts - attempts} attempts left)")
            else:
                print(f"📈 Too high. Try again. ({max_attempts - attempts} attempts left)")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue
    
    print(f"\n😞 Game Over! The secret number was {secret}.")
    return False

def main():
    """Main game loop."""
    print("=" * 50)
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("=" * 50)
    
    while True:
        print("\n📊 Select Difficulty Level:")
        print("1. Easy (1-10, 5 attempts)")
        print("2. Medium (1-50, 8 attempts)")
        print("3. Hard (1-100, 10 attempts)")
        
        try:
            difficulty = int(input("\nEnter your choice (1-3): "))
            if difficulty not in [1, 2, 3]:
                print("⚠️  Please enter 1, 2, or 3.")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue
        
        # Play the game
        play_game(difficulty)
        
        # Ask if they want to play again
        while True:
            replay = input("\n🔄 Do you want to play again? (yes/no): ").lower().strip()
            if replay in ['yes', 'y']:
                break
            elif replay in ['no', 'n']:
                print("\n👋 Thanks for playing! Goodbye!")
                return
            else:
                print("⚠️  Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
