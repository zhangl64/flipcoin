from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt
import random

def quantum_coin_flip(classical_guess):
    qc = QuantumCircuit(1, 1)

    # Step 1: Quantum player sets coin into superposition
    qc.h(0)

    # Step 2: Quantum player explicitly forces opposite outcome
    if classical_guess == 1:
        # Human guessed '1' (tails), force outcome to '0' (heads)
        qc.reset(0)     # Reset the superposition state to |0⟩
    else:
        # Human guessed '0' (heads), force outcome to '1' (tails)
        qc.reset(0)     # Reset to |0⟩ first
        qc.x(0)         # Then flip to |1⟩ explicitly

    # Measure to get the forced outcome
    qc.measure(0, 0)
    backend = Aer.get_backend('qasm_simulator')
    job = backend.run(qc, shots=1)
    result = job.result()
    outcome = int(list(result.get_counts().keys())[0])

    return outcome

# Run 1000 trials to visualize clearly
rounds = 1000
quantum_wins, classical_wins = 0, 0

for _ in range(rounds):
    classical_guess = random.choice([0, 1])
    outcome = quantum_coin_flip(classical_guess)

    if classical_guess != outcome:
        quantum_wins += 1
    else:
        classical_wins += 1  # ideally never happens

# Visualization
labels = ['Quantum Player Wins', 'Classical Player Wins']
results = [quantum_wins, classical_wins]

plt.figure(figsize=(8, 6))
plt.bar(labels, results, color=['blue', 'orange'])
plt.ylabel('Number of Wins')
plt.title('Quantum vs Classical Player: 1000 Coin Flips')
plt.text(0, quantum_wins + 20, str(quantum_wins), ha='center', fontsize=12)
plt.text(1, classical_wins + 20, str(classical_wins), ha='center', fontsize=12)
plt.ylim(0, rounds + 50)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()