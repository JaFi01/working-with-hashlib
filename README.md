# File Hash Visualization and Verification

This project consists of two Python scripts: `main.py` and `program_hash.py`, each serving different purposes.

## Main.py

This script (`main.py`) visualizes the time needed to encrypt a given phrase using various hashing algorithms available in the `hashlib` module. It generates a bar chart using Plotly to represent the encryption time for each algorithm.

### Usage

1. Install the required dependencies by running:
   `pip install -r requirements.txt`
2. Run the script using Python:
    `python main.py`
3. Follow the prompts to input a phrase and visualize the encryption time for each algorithm.

## Program_hash.py

This script (`program_hash.py`) verifies whether a specific Linux ISO file (`linuxmint-21.3-xfce-64bit.iso`) has the correct SHA-256 hash. The hash value is compared with the expected hash value (`CORRECT_HASH`) defined in the script.

### Usage

1. Ensure that the correct Linux ISO file (`linuxmint-21.3-xfce-64bit.iso`) is present in the specified path (in my case-) (`/mnt/c/Users/jaros/Downloads/`).

2. Run the script using Python:
    `python program_hash.py`
3. Follow the prompts to choose whether to verify the hash or to read the hash of the file.


## Requirements

- Python 3.x
- Plotly
