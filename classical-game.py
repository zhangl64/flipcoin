#!/usr/bin/env python3
"""
Classical Coin Flip Game: Play until you choose to quit.

Type '0' for heads, '1' for tails, or 'exit'/'quit' to stop.
Press Ctrl+C to exit at any time.
"""

# import sys
import random

def classical_coin_flip() -> int:
    """Simulate a fair coin flip: 0=heads, 1=tails."""
    return random.choice([0, 1])

def main():
    print("🪙 Classical Coin Flip Game 🪙")
    print("Enter '0' for heads, '1' for tails, or 'exit' to quit.")
    
    while True:
        try:
            user_input = input("\nYour guess [0/1 or 'exit']: ").strip().lower()
            if user_input in ('exit', 'quit'):
                print("👋 Thanks for playing! Goodbye.")
                break
            if user_input not in ('0', '1'):
                print("⚠️  Invalid input. Please enter 0, 1, or 'exit'.")
                continue

            guess = int(user_input)
            outcome = classical_coin_flip()
            outcome_str = 'heads (0)' if outcome == 0 else 'tails (1)'
            print(f"🎲 The coin landed on: {outcome_str}")

            if outcome == guess:
                print("🎉 You win!")
            else:
                print("🙂 Computer wins!")
        except KeyboardInterrupt:
            print("\n\n✋ Interrupted. Goodbye.")
            break
        except Exception as e:
            print(f"⚠️  Unexpected error: {e}")
            break

if __name__ == "__main__":
    main()