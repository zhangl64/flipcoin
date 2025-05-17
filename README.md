# Quantum vs Classical Coin Flip Game

This repository contains two interactive Python scripts:

* **`quantum-game.py`**: A quantum-powered coin flip that always forces the opposite of the user's guess using Qiskit Aer.
* **`classical-game.py`**: A classical coin flip simulation where the outcome is random and either the user or the computer can win.

Both games run in a loop, prompting the user to enter `0` (heads), `1` (tails), or `exit`/`quit` to end the game.

## Features

* **Quantum Coin Flip**

  * Uses Qiskit and AerSimulator to create a superposition, then forces the qubit to the opposite state of the user's guess.
  * Demonstrates quantum state preparation, reset, and measurement.

* **Classical Coin Flip**

  * Simulates a fair coin toss with Python's `random.choice`.
  * Illustrates a true 50/50 chance game.

## Requirements

* Python 3.8 or later
* `qiskit` (Terra & Aer)
* `qiskit-aer`
* `qiskit-ibm-runtime`
* `matplotlib` (optional, only for batch experiments and plotting)

You can install all dependencies with:

```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime matplotlib
```

## Usage

### Quantum Game

```bash
python quantum-game.py
```

**Prompt:**

```
🔮 Quantum Coin Flip Game 🔮
Enter '0' for heads, '1' for tails, or 'exit' to quit.
```

### Classical Game

```bash
python classical-game.py
```

**Prompt:**

```
🪙 Classical Coin Flip Game 🪙
Enter '0' for heads, '1' for tails, or 'exit' to quit.
```

## Switching Backends in Quantum Game

By default the quantum game uses the local `AerSimulator`. To run on a real IBM Quantum device, edit the backend definition at the top of `flipcoin-ibmq.py`, i.e.,

```python
from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService()
backend = service.backend("ibm_brisbane")
```

Make sure you have saved your IBM Quantum API token via:

```python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(token="YOUR_TOKEN", channel="ibm_quantum", overwrite=True)
```

## Batch Experiments & Noise Simulation

For more advanced batch experiments with customizable backends (simulator, noisy simulator, or real IBM Quantum devices), see the `flipcoin-ibmq.py` script. This script allows you to:

* Define your backend once at the top (Aer simulator, noisy model via fake/backends, or real IBMQ devices).
* Run a large number of trials (default 1000, or any integer you specify).
* Automatically count quantum vs. classical wins and print execution timing statistics.
* Optionally collect and plot results using Matplotlib.

Example usage:

```bash
python flipcoin-ibmq.py        # Runs the default 1000 trials and plots the win counts
python flipcoin-ibmq.py 5000   # Run 5000 trials (if script updated to accept command-line arg)
```

This script is ideal for performance benchmarking and noise-characterization studies.

## Noisy Quantum Machine

For statistical demonstrations, use `run_experiment()` in the batch script (e.g., 1000 trials) and plot results with Matplotlib. You can also simulate device noise by swapping the backend to a fake/noisy model:

```python
from qiskit.providers.fake_provider import FakeVigo  # or FakeBrisbane
from qiskit_aer import AerSimulator
backend = AerSimulator.from_backend(FakeVigo())
```

## Contributing

ChatGPT was used to assist code generation. Feel free to open issues or submit pull requests to improve the games, add new features, or adjust noise models.

## License

This project is released under the MIT License. Feel free to use and adapt as you like.
