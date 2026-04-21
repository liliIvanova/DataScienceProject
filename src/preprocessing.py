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


#def convert_dataset(hex_lines):
#    return [hex_to_bits(h) for h in hex_lines]

def convert_dataset(hex_lines, block_size=128):
    # 1. Join all hex strings into one long bit string
    # We use a generator expression for memory efficiency
    all_bits_str = "".join(
        format(int(h[i:i+2], 16), '08b') 
        for h in hex_lines 
        for i in range(0, len(h), 2)
    )
    
    # 2. Use np.fromiter with a map to ensure clean 0s and 1s
    # This converts each '0'/'1' char directly to an integer 0/1
    bit_array = np.fromiter(map(int, all_bits_str), dtype=np.uint8)
    
    # 3. Reshape into your feature matrix
    return bit_array.reshape(-1, block_size)



    
def group_sequences(data, blocks_to_merge=8):
    # 1. Calculate how many full large blocks we can make
    n_rows, bits_per_row = data.shape
    n_new_rows = n_rows // blocks_to_merge
    
    # 2. Trim the data so it's a perfect multiple
    trimmed_data = data[:n_new_rows * blocks_to_merge]
    
    # 3. Reshape into larger chunks
    # This glues 'blocks_to_merge' rows together into one long row
    return trimmed_data.reshape(n_new_rows, -1)
    
    
def train_test_split_sequences(data, train_ratio=0.8):
    split_idx = int(len(data) * train_ratio)
    
    train = data[:split_idx]
    test = data[split_idx:]
    
    return train, test