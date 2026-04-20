import yaml
import numpy as np


def load_hex_lines(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    lines = [line.strip() for line in lines if line.strip() != ""]
    return lines

  
def hex_to_bits(hex_input):
    """
    Converts a string of hex pairs (space/newline separated) 
    into a NumPy array of bits (0s and 1s).
    """
    # 1. Split by whitespace (handles both spaces and newlines)
    hex_values = hex_input.split()
    
    # 2. Convert each 2-symbol hex to a 8-bit binary string
    # '08b' ensures leading zeros are kept for a full byte
    bit_string = "".join(format(int(h, 16), '08b') for h in hex_values)
    
    # 3. Convert characters '0'/'1' to an array of integers
    return np.array([int(b) for b in bit_string], dtype=np.uint8)


def convert_dataset(hex_lines):
    return [hex_to_bits(h) for h in hex_lines]


def group_sequences(data, group_size=8):
    grouped = []
    
    for i in range(0, len(data) - group_size, group_size):
        chunk = np.concatenate(data[i:i+group_size])
        grouped.append(chunk)
    
    return grouped
    

def train_test_split_sequences(data, train_ratio=0.8):
    split_idx = int(len(data) * train_ratio)
    
    train = data[:split_idx]
    test = data[split_idx:]
    
    return train, test