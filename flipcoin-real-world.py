#!/usr/bin/env python3
"""
Classical Coin Flip Battle

Simulates N rounds where the player randomly calls 0 (heads) or 1 (tails),
and a fair coin is flipped.  Tracks player wins vs. house wins.
"""

import sys
import random
import matplotlib.pyplot as plt

def simulate_battle(rounds: int) -> (int, int):
    """Simulate `rounds` coin flips with random player calls."""
    player_wins = 0
    house_wins  = 0
    for _ in range(rounds):
        call = random.choice([0, 1])   # player's guess
        flip = random.choice([0, 1])   # actual coin flip
        if call == flip:
            player_wins += 1
        else:
            house_wins += 1
    return player_wins, house_wins

def main():
    print("🪙 Classical Coin Flip Battle 🪙")
    print("Enter how many rounds to simulate, or 'exit' to quit.")

    while True:
        inp = input("\nNumber of rounds: ").strip().lower()
        if inp in ("exit", "quit"):
            print("👋 Goodbye.")
            sys.exit(0)
        try:
            rounds = int(inp)
            if rounds <= 0:
                raise ValueError()
        except ValueError:
            print("⚠️  Please enter a positive integer or 'exit'.")
            continue

        # Run the battle
        p_wins, h_wins = simulate_battle(rounds)
        print(f"\nResults over {rounds} rounds:")
        print(f"  Player wins: {p_wins} ({p_wins/rounds:.2%})")
        print(f"  House wins : {h_wins} ({h_wins/rounds:.2%})")

        # Plot only the win counts
        labels = ["Player wins", "House wins"]
        counts = [p_wins, h_wins]

        plt.figure(figsize=(6,4))
        plt.bar(labels, counts, color=["skyblue","salmon"])
        plt.ylabel("Number of Wins")
        plt.title(f"Player vs House over {rounds} Rounds")
        for i, c in enumerate(counts):
            plt.text(i, c + rounds*0.01, str(c), ha="center")
        plt.ylim(0, rounds * 1.1)
        plt.grid(axis="y", linestyle="--", alpha=0.4)
        plt.show()

        again = input("Run another battle? [Y/n]: ").strip().lower()
        if again in ("n", "no"):
            print("👋 Goodbye.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✋ Interrupted. Goodbye.")
        sys.exit(0)