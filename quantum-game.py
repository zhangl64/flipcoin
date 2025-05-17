#!/usr/bin/env python3
"""
Quantum Coin Flip Game: Play until you choose to quit.

Type '0' for heads, '1' for tails, or 'exit'/'quit' to stop.
Press Ctrl+C to exit at any time.
"""

import sys
import random
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Initialize local simulator backend
backend = AerSimulator()

def quantum_coin_flip(classical_guess: int) -> int:
    """Perform one quantum coin flip that always yields the opposite of classical_guess."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)         # fair quantum coin
    qc.reset(0)     # clear any prior state
    if classical_guess == 0:
        qc.x(0)     # force |1> (tails) if guess was heads
    qc.measure(0, 0)

    job = backend.run(qc, shots=1)
    counts = job.result().get_counts()
    return int(next(iter(counts)))

def main():
    print("🔮 Quantum Coin Flip Game 🔮")
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
            outcome = quantum_coin_flip(guess)
            outcome_str = 'heads (0)' if outcome == 0 else 'tails (1)'
            print(f"🎲 Quantum coin result: {outcome_str}")

            if outcome != guess:
                print("🎉 Quantum player wins!")
            else:
                print("🙂 Classical player wins!")
        except KeyboardInterrupt:
            print("\n\n✋ Interrupted. Goodbye.")
            break
        except Exception as e:
            print(f"⚠️  Unexpected error: {e}")
            break

if __name__ == "__main__":
    main()