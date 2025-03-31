import random

def generate_key(seed=None):
    """
    Generate a pseudo-random key for encryption
    
    Args:
        seed (int, optional): Seed for the random number generator
        
    Returns:
        int: A random integer between 1 and 25
    """
    if seed is not None:
        random.seed(seed)
    return random.randint(1, 25)

def encrypt_text(plaintext, key):
    """
    Encrypt plaintext using the Cyber Yantra substitution cipher
    
    Args:
        plaintext (str): The text to encrypt
        key (int): The encryption key (shift value)
        
    Returns:
        str: The encrypted text
    """
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Get the position in the alphabet (0-25)
            position = ord(char) - ascii_offset
            # Apply shift with modular arithmetic
            new_position = (position + key) % 26
            # Convert back to character
            ciphertext += chr(new_position + ascii_offset)
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
            
    return ciphertext

def decrypt_text(ciphertext, key):
    """
    Decrypt ciphertext using the Cyber Yantra substitution cipher
    
    Args:
        ciphertext (str): The text to decrypt
        key (int): The encryption key (shift value)
        
    Returns:
        str: The decrypted text
    """
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Get the position in the alphabet (0-25)
            position = ord(char) - ascii_offset
            # Apply inverse shift with modular arithmetic
            # Add 26 to ensure the result is positive before applying modulus
            original_position = (position - key + 26) % 26
            # Convert back to character
            plaintext += chr(original_position + ascii_offset)
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char
            
    return plaintext

def encrypt_file(file_content, key):
    """
    Encrypt the content of a file
    
    Args:
        file_content (str): The content of the file
        key (int): The encryption key
        
    Returns:
        str: The encrypted content
    """
    return encrypt_text(file_content, key)

def decrypt_file(encrypted_content, key):
    """
    Decrypt the content of a file
    
    Args:
        encrypted_content (str): The encrypted content
        key (int): The encryption key
        
    Returns:
        str: The decrypted content
    """
    return decrypt_text(encrypted_content, key)

# Custom functions for enhanced versions of Cyber Yantra

def poly_encrypt(plaintext, keys):
    """
    Polyalphabetic encryption - uses multiple keys in sequence
    
    Args:
        plaintext (str): The text to encrypt
        keys (list): List of encryption keys to use in sequence
        
    Returns:
        str: The encrypted text
    """
    ciphertext = ""
    key_index = 0
    key_length = len(keys)
    
    for char in plaintext:
        if char.isalpha():
            # Get the current key from the sequence
            current_key = keys[key_index % key_length]
            key_index += 1
            
            ascii_offset = ord('A') if char.isupper() else ord('a')
            position = ord(char) - ascii_offset
            new_position = (position + current_key) % 26
            ciphertext += chr(new_position + ascii_offset)
        else:
            ciphertext += char
            
    return ciphertext

def poly_decrypt(ciphertext, keys):
    """
    Polyalphabetic decryption - uses multiple keys in sequence
    
    Args:
        ciphertext (str): The text to decrypt
        keys (list): List of decryption keys to use in sequence
        
    Returns:
        str: The decrypted text
    """
    plaintext = ""
    key_index = 0
    key_length = len(keys)
    
    for char in ciphertext:
        if char.isalpha():
            # Get the current key from the sequence
            current_key = keys[key_index % key_length]
            key_index += 1
            
            ascii_offset = ord('A') if char.isupper() else ord('a')
            position = ord(char) - ascii_offset
            original_position = (position - current_key + 26) % 26
            plaintext += chr(original_position + ascii_offset)
        else:
            plaintext += char
            
    return plaintext
