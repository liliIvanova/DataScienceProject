import secrets
import random
import numpy as np

def generate_cs_prng_hex(file_path, n_numbers=10000, bits=128):
    """
    Generate n_numbers cryptographically secure random numbers
    with length 'bits' bits and write them in hex format to a file.
    """
    # Convert bits to bytes
    n_bytes = bits // 8
    generated_numbers = []
    
    with open(file_path, "w") as f:
        for _ in range(n_numbers):
            # Generate random number with n_bytes length
            rand_bytes = secrets.token_bytes(n_bytes)
            hex_str = rand_bytes.hex()
            f.write(hex_str + "\n")
            generated_numbers.append(hex_str)
    return generated_numbers
    
    

            
def generate_bit_array_npy(file_path, total_bits=1000000, block_size=128, seed=42):
    """
    Generate array of 0s and 1s and writes it to .npy file.
    """
    random.seed(seed)
    
    # 1. Generate bit sequence, convert it to array of bytes (for faster processing)
    n_blocks = total_bits // block_size
    adjusted_total_bits = n_blocks * block_size
    
    total_bytes = (adjusted_total_bits + 7) // 8
    bits = random.getrandbits(adjusted_total_bits)
    byte_data = bits.to_bytes(total_bytes, byteorder='big')
    
    # 2. Convert bytes into NumPy array of uint8
    byte_array = np.frombuffer(byte_data, dtype=np.uint8)
    
    # 3. "Unpack" every byte into 8 separate bits (0 и 1)
    bit_array = np.unpackbits(byte_array)[:adjusted_total_bits]
    # 4. Transform bit array into arrays of blocks with size block_size
    bit_blocks = bit_array.reshape(-1, block_size)
    
    # 5. write bit array to the output file
    np.save(file_path, bit_blocks)
    return bit_blocks