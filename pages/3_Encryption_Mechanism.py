import streamlit as st
import pandas as pd
import numpy as np
import io

# Configure page
st.set_page_config(
    page_title="Encryption Mechanism - Cyber Yantra",
    page_icon="🔐",
    layout="wide"
)

# Title
st.title("Cyber Yantra Encryption Mechanism")
st.markdown("## Understanding How the Encryption Works")

# Introduction
st.markdown("""
Cyber Yantra uses a novel grid-based substitution cipher that improves upon classical 
cipher techniques. This page explains the encryption mechanism and allows you to try it out.
""")

# Cyber Yantra Grid
st.subheader("The Cyber Yantra Grid")

# Create and display the grid
grid_data = [
    ["", "1", "2", "3", "4", "5"],
    ["1", "A", "B", "C", "D", "E"],
    ["2", "F", "G", "H", "I", "J"],
    ["3", "K", "L", "M", "N", "O"],
    ["4", "P", "Q", "R", "S", "T"],
    ["5", "U", "V", "W", "X", "Y/Z"]
]

# Convert to DataFrame for better display
grid_df = pd.DataFrame(grid_data)

# Style the grid
st.markdown("""
<style>
    .cyber-grid {
        color: #333;
        font-size: 1.2rem;
        text-align: center;
    }
    .cyber-grid th {
        background-color: #ffcccb;
        font-weight: bold;
    }
    .cyber-grid td {
        background-color: #f0f5ff;
        width: 60px;
        height: 60px;
        text-align: center;
    }
    .cyber-grid tr:first-child td {
        background-color: #ffcccb;
        font-weight: bold;
    }
    .cyber-grid tr td:first-child {
        background-color: #ffcccb;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Display the grid with styling
st.table(grid_df.style.set_table_attributes('class="cyber-grid"'))

st.markdown("""
### How the Grid Works

The Cyber Yantra grid represents a 5x5 encryption matrix where:
- Each letter of the alphabet (A-Z) is mapped to a specific position
- Y and Z share the same cell (5,5) due to the 5x5 limitation
- Each position can be represented as a pair of coordinates (row, column)
- These coordinates become the encrypted form of the letter
""")

# Define encryption and decryption functions for the grid
def get_grid_position(char):
    """Convert a character to its grid position"""
    char = char.upper()
    
    if char == 'Z':  # Z shares position with Y
        char = 'Y'
    
    # Define the grid mapping
    grid = {
        'A': (1, 1), 'B': (1, 2), 'C': (1, 3), 'D': (1, 4), 'E': (1, 5),
        'F': (2, 1), 'G': (2, 2), 'H': (2, 3), 'I': (2, 4), 'J': (2, 5),
        'K': (3, 1), 'L': (3, 2), 'M': (3, 3), 'N': (3, 4), 'O': (3, 5),
        'P': (4, 1), 'Q': (4, 2), 'R': (4, 3), 'S': (4, 4), 'T': (4, 5),
        'U': (5, 1), 'V': (5, 2), 'W': (5, 3), 'X': (5, 4), 'Y': (5, 5)
    }
    
    if char in grid:
        return grid[char]
    else:
        return None

def get_char_from_position(row, col):
    """Convert grid position to character"""
    # Define the reverse grid mapping
    reverse_grid = {
        (1, 1): 'A', (1, 2): 'B', (1, 3): 'C', (1, 4): 'D', (1, 5): 'E',
        (2, 1): 'F', (2, 2): 'G', (2, 3): 'H', (2, 4): 'I', (2, 5): 'J',
        (3, 1): 'K', (3, 2): 'L', (3, 3): 'M', (3, 4): 'N', (3, 5): 'O',
        (4, 1): 'P', (4, 2): 'Q', (4, 3): 'R', (4, 4): 'S', (4, 5): 'T',
        (5, 1): 'U', (5, 2): 'V', (5, 3): 'W', (5, 4): 'X', (5, 5): 'Y'  # Note: Z also maps to (5,5)
    }
    
    pos = (row, col)
    if pos in reverse_grid:
        return reverse_grid[pos]
    else:
        return None

def encrypt_grid(text):
    """Encrypt text using the Cyber Yantra grid"""
    encrypted = []
    
    for char in text:
        if char.isalpha():
            position = get_grid_position(char)
            if position:
                row, col = position
                encrypted.append(f"{row}{col}")
        else:
            # Keep non-alphabetic characters as they are
            encrypted.append(char)
    
    return ' '.join(encrypted)

def decrypt_grid(text):
    """Decrypt text using the Cyber Yantra grid"""
    decrypted = []
    
    # Split the text by spaces to get coordinate pairs
    parts = text.split()
    
    for part in parts:
        if len(part) == 2 and part.isdigit():
            row, col = int(part[0]), int(part[1])
            if 1 <= row <= 5 and 1 <= col <= 5:
                char = get_char_from_position(row, col)
                if char:
                    decrypted.append(char)
        else:
            # Keep non-coordinate parts as they are
            decrypted.append(part)
    
    return ''.join(decrypted)

# Interactive demo
st.subheader("Try the Cyber Yantra Encryption")

tabs = st.tabs(["Text to Coordinates", "Coordinates to Text", "Advanced Coding"])

with tabs[0]:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Input")
        user_input = st.text_area("Enter text (a-z, A-Z):", "HELLO WORLD", height=100)
        encrypt_button = st.button("Encrypt", key="encrypt_btn")
    
    with col2:
        st.markdown("### Output")
        if encrypt_button and user_input:
            encrypted = encrypt_grid(user_input)
            st.text_area("Encrypted coordinates:", encrypted, height=100)
            
            # Create visualization of the encryption
            if user_input and len(user_input) > 0:
                st.markdown("### Encryption Visualization")
                
                # Create mapping data
                mapping_data = []
                for char in user_input:
                    if char.isalpha():
                        position = get_grid_position(char)
                        if position:
                            row, col = position
                            mapping_data.append({
                                "Original Character": char.upper(),
                                "Grid Position": f"({row}, {col})",
                                "Encrypted Form": f"{row}{col}"
                            })
                    else:
                        mapping_data.append({
                            "Original Character": char,
                            "Grid Position": "N/A",
                            "Encrypted Form": char
                        })
                
                # Display mapping
                mapping_df = pd.DataFrame(mapping_data)
                st.table(mapping_df)

with tabs[1]:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Input")
        coord_input = st.text_area("Enter coordinates (e.g., 11 22 33):", "23 15 12 12 34", height=100)
        decrypt_button = st.button("Decrypt", key="decrypt_btn")
    
    with col2:
        st.markdown("### Output")
        if decrypt_button and coord_input:
            decrypted = decrypt_grid(coord_input)
            st.text_area("Decrypted text:", decrypted, height=100)
            
            # Create visualization of the decryption
            if coord_input and len(coord_input) > 0:
                st.markdown("### Decryption Visualization")
                
                # Create mapping data
                mapping_data = []
                parts = coord_input.split()
                
                for part in parts:
                    if len(part) == 2 and part.isdigit():
                        row, col = int(part[0]), int(part[1])
                        if 1 <= row <= 5 and 1 <= col <= 5:
                            char = get_char_from_position(row, col)
                            mapping_data.append({
                                "Coordinate": part,
                                "Grid Position": f"({row}, {col})",
                                "Decrypted Character": char
                            })
                    else:
                        mapping_data.append({
                            "Coordinate": part,
                            "Grid Position": "N/A",
                            "Decrypted Character": part
                        })
                
                # Display mapping
                mapping_df = pd.DataFrame(mapping_data)
                st.table(mapping_df)

with tabs[2]:
    st.markdown("""
    ### Advanced Cyber Yantra Coding
    
    For enhanced security, Cyber Yantra can incorporate additional techniques:
    
    1. **Key-based Row/Column Shifting**: Apply a numeric key to shift grid positions
    2. **Transposition**: Rearrange the order of coordinates
    3. **Padding**: Add decoy coordinates to obscure message length
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        advanced_input = st.text_area("Enter text:", "SECRET MESSAGE", height=80)
        shift_key = st.slider("Shift Key (0-4):", 0, 4, 2)
        add_padding = st.checkbox("Add random padding", value=True)
        advanced_encrypt = st.button("Apply Advanced Encryption", key="adv_encrypt")
    
    with col2:
        if advanced_encrypt and advanced_input:
            # Basic encryption first
            basic_encrypted = encrypt_grid(advanced_input)
            
            # Apply shift based on key (simplified example)
            parts = basic_encrypted.split()
            shifted_parts = []
            
            for part in parts:
                if len(part) == 2 and part.isdigit():
                    row = (int(part[0]) + shift_key) % 5
                    col = (int(part[1]) + shift_key) % 5
                    # Ensure we don't have 0 as row/col
                    row = 5 if row == 0 else row
                    col = 5 if col == 0 else col
                    shifted_parts.append(f"{row}{col}")
                else:
                    shifted_parts.append(part)
            
            # Add padding if selected
            if add_padding:
                import random
                # Add 2-4 random coordinates as padding
                padding_count = random.randint(2, 4)
                for _ in range(padding_count):
                    # Insert at random positions
                    pos = random.randint(0, len(shifted_parts))
                    row = random.randint(1, 5)
                    col = random.randint(1, 5)
                    shifted_parts.insert(pos, f"{row}{col}")
            
            advanced_encrypted = ' '.join(shifted_parts)
            
            st.text_area("Advanced Encrypted Result:", advanced_encrypted, height=80)
            st.info(f"""
            This advanced encryption:
            1. Converted text to grid coordinates
            2. Applied a shift of {shift_key} to each coordinate
            3. {"Added random padding to obscure message length" if add_padding else "No padding was added"}
            
            For decryption, the receiver would need to know:
            - The shift key: {shift_key}
            - Whether padding was used: {"Yes" if add_padding else "No"}
            """)

# Mathematical explanation
st.subheader("The Mathematics Behind Cyber Yantra")

st.markdown("""
### Encryption Formula

For each alphabetic character in the plaintext, Cyber Yantra applies the following transformation:

$$C_i = (P_i + K) \mod 26$$

Where:
- $C_i$ is the position of the encrypted character in the alphabet (0-25)
- $P_i$ is the position of the original character in the alphabet (0-25)
- $K$ is the encryption key (a number between 1 and 25)
- $\mod 26$ ensures the result wraps around the alphabet

### Decryption Formula

To decrypt, the inverse operation is applied:

$$P_i = (C_i - K + 26) \mod 26$$

The addition of 26 ensures the result remains positive before applying the modulus operation.

### Polyalphabetic Enhancement

In the enhanced version, multiple keys are used in sequence:

$$C_i = (P_i + K_{i \mod m}) \mod 26$$

Where $K_{i \mod m}$ represents the key used for the $i$-th character, cycling through $m$ different keys.
""")

# Security considerations
st.subheader("Security Considerations")

st.markdown("""
### Strengths

- **Visual Simplicity**: The grid makes encryption visually intuitive
- **Numerical Output**: Converts letters to numbers, adding a layer of obscurity
- **Flexible Enhancement**: Can be combined with other techniques (shifting, padding, etc.)
- **Educational Value**: Demonstrates substitution and transposition concepts clearly

### Limitations

- **Limited Character Set**: Basic grid only handles 25 characters (Y/Z share position)
- **Fixed Grid**: Standard grid arrangement could be vulnerable to frequency analysis
- **Coordinate Pattern**: Two-digit patterns might reveal information about letter positions

### Appropriate Use Cases

- **Educational Settings**: Teaching fundamental cryptography concepts
- **Puzzles and Games**: Creating engaging cipher challenges
- **Basic Information Hiding**: Simple protection for non-sensitive communications
- **Paper-Based Encryption**: Can be performed without computational tools

For highly sensitive information, industry-standard encryption like AES or RSA is recommended.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <small>
        This implementation is based on the Cyber Yantra research paper.<br>
        For critical applications, please use established encryption standards like AES, RSA, or other industry-accepted protocols.
    </small>
</div>
""", unsafe_allow_html=True)
