#!/usr/bin/env python3
import time
import datetime
import random
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit_ibm_runtime.fake_provider import FakeBrisbane, FakeVigoV2
# or FakeToronto, FakeMontreal, FakeCasablanca, …  


# === BACKEND DEFINITION (modify ONLY this block) ===

# Real IBM Quantum device (comment out Option A first)
service = QiskitRuntimeService()
# service = QiskitRuntimeService(channel="ibm_quantum")

# # Fetch all available backends
# all_backends = service.backends()
# # Print their names
# print("Available quantum machines:")
# for backend in all_backends:
#     print("->", backend.name)

# Option A: real quantum device , choose one of the following
# backend = service.backend("ibm_brisbane")
# backend = service.backend("ibm_strasbourg")
# backend = service.least_busy(simulator=False,operational=True)

# Option B: simulator with noise model from real device
# real_backend = service.backend("ibm_brisbane")
# backend = AerSimulator.from_backend(real_backend)  
# print("Using AerSimulator with noise model from real device.")

# Optional C: Local Aer simulator with no noise
# backend = AerSimulator()
# print("Using AerSimulator with no noise.")

# Option D: Local Aer simulator: Fake backend
# Swap this in place of your real-device‐derived backend:
backend = AerSimulator.from_backend(FakeVigoV2())
print("Simulating with extremely noisy model.")

# For AerSimulator (BackendV2) or IBMRuntimeBackend
try:
    backend_name = backend.name()
except TypeError:
    # Older backends expose .name as a property
    backend_name = backend.name

print(f"Using backend: {backend_name}")
# === END BACKEND DEFINITION ===


def quantum_coin_flip(classical_guess: int) -> int:
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.reset(0)
    if classical_guess == 0:
        qc.x(0)
    qc.measure(0, 0)

    transpiled = transpile(qc, backend=backend)

    # **branch depending on type of backend**
    if isinstance(backend, AerSimulator):
        # Local (no Runtime): use execute()
        #job    = execute(transpiled, backend=backend, shots=1)
        job = backend.run(transpiled, shots=1)
        counts = job.result().get_counts()
    else:
        # Real hardware via Runtime primitives
        with Session(backend=backend):
            sampler = Sampler()
            job     = sampler.run([transpiled], shots=1)
            result  = job.result()
        
        # estimate the job usage
        # print(job.usage_estimation)
        print("Estimated QPU time:", job.usage_estimation)

        # And for actual run time:
        usage = job.metrics()["usage"]
        print("Actual QPU usage (s):", usage)

        counts = result[0].data.c.get_counts()
    
    # Get the outcome from the counts
    bit    = next(iter(counts))
    return int(bit)


def run_experiment(trials: int = 1000):
    q_wins, c_wins = 0, 0
        
    start_time = time.time()

    for _ in range(trials):
        guess   = random.choice([0, 1])
        outcome = quantum_coin_flip(guess)
        if outcome != guess:
            q_wins += 1
        else:
            c_wins += 1
    
    end_time = time.time()

    elapsed_seconds = end_time - start_time
    formatted_time = str(datetime.timedelta(seconds=elapsed_seconds))
    print(f"Execution time: {formatted_time}")

    print(f'Classical wins: {c_wins} vs. Quantum wins: {q_wins}')

    return q_wins, c_wins


if __name__ == '__main__':
    # # Run a quick single‐trial demo
    # g = random.choice([0, 1])
    # o = quantum_coin_flip(g)
    # print(f'Classical guess: {g} → Quantum outcome: {o} →',
    #       'Quantum wins!' if o != g else 'Classical wins!')

    # Then run the full experiment
    trials = 10
    q_wins, c_wins = run_experiment(trials)

    # Plot results
    plt.bar(
        ['Quantum wins', 'Classical wins'],
        [q_wins, c_wins],
        color=['teal', 'gray']
    )
    plt.ylabel('Number of Wins')
    plt.title(f'Quantum vs Classical over {trials} Trials')
    plt.text(0, q_wins + trials*0.01, str(q_wins), ha='center')
    plt.text(1, c_wins + trials*0.01, str(c_wins), ha='center')
    plt.ylim(0, trials + trials*0.05)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()
