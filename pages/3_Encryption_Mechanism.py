import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from cyber_yantra import encrypt_text, decrypt_text, poly_encrypt, poly_decrypt

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
Cyber Yantra builds upon classical substitution cipher principles while incorporating enhancements
that improve security. This page explains the encryption mechanism and allows you to see it in action.
""")

# Encryption Mechanism Explanation
st.subheader("How the Algorithm Works")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    ### Core Principles
    
    Cyber Yantra uses a substitution cipher enhanced with:
    
    1. **Dynamic Key Generation**: 
       - A pseudo-random number generator (PRNG) creates a unique key for each encryption session
       - This approach reduces predictability compared to static keys
    
    2. **Character-by-Character Processing**:
       - Each alphabetic character is shifted based on its position and the key
       - Non-alphabetic characters (numbers, punctuation, etc.) remain unchanged
    
    3. **Modular Arithmetic**:
       - The shift operation uses modulo 26 (for the English alphabet)
       - This ensures the result wraps around the alphabet properly
    
    4. **Enhanced Versions (Optional)**:
       - Polyalphabetic substitution: uses multiple keys in sequence
       - This further complicates frequency analysis attacks
    """)

with col2:
    # Simplified algorithm flowchart
    st.markdown("### Algorithm Flowchart")
    
    flowchart = """
    ```mermaid
    graph TD
        A[Start] --> B[Generate Key]
        B --> C[Process Input Text]
        C --> D{Is Character Alphabetic?}
        D -- Yes --> E[Calculate Position in Alphabet]
        D -- No --> F[Keep Character Unchanged]
        E --> G[Apply Shift: new_pos = (pos + key) mod 26]
        G --> H[Convert to New Character]
        H --> I[Add to Ciphertext]
        F --> I
        I --> J{More Characters?}
        J -- Yes --> C
        J -- No --> K[Return Ciphertext]
        K --> L[End]
    ```
    """
    
    st.markdown(flowchart)

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

# Interactive demonstration
st.subheader("Try the Encryption Tool")

demo_tab1, demo_tab2 = st.tabs(["Basic Encryption", "Advanced (Polyalphabetic)"])

with demo_tab1:
    col_input, col_output = st.columns(2)
    
    with col_input:
        st.markdown("### Input")
        user_input = st.text_area("Enter text to encrypt:", 
                                  "The quick brown fox jumps over the lazy dog.", 
                                  height=100)
        key = st.slider("Select encryption key (1-25):", 1, 25, 7)
        
        encrypt_button = st.button("Encrypt")
        
    with col_output:
        st.markdown("### Output")
        
        if encrypt_button and user_input:
            encrypted = encrypt_text(user_input, key)
            st.text_area("Encrypted text:", encrypted, height=100)
            
            # Show decryption option
            if st.button("Decrypt"):
                decrypted = decrypt_text(encrypted, key)
                st.text_area("Decrypted text:", decrypted, height=100)
            
            # Show character mapping
            st.markdown("### Character Mapping")
            
            # Create a mapping table for the first few characters
            mapping_data = []
            sample_text = user_input[:10] if len(user_input) > 10 else user_input
            sample_encrypted = encrypted[:10] if len(encrypted) > 10 else encrypted
            
            for i, (p, c) in enumerate(zip(sample_text, sample_encrypted)):
                if p.isalpha():
                    p_pos = ord(p.lower()) - ord('a')
                    c_pos = ord(c.lower()) - ord('a')
                    shift = (c_pos - p_pos) % 26
                    mapping_data.append({
                        "Original": p,
                        "Position": p_pos,
                        "Shift": f"+{shift}",
                        "New Position": c_pos,
                        "Encrypted": c
                    })
                else:
                    mapping_data.append({
                        "Original": p,
                        "Position": "N/A",
                        "Shift": "N/A",
                        "New Position": "N/A",
                        "Encrypted": p
                    })
            
            mapping_df = pd.DataFrame(mapping_data)
            st.table(mapping_df)

with demo_tab2:
    col_adv_input, col_adv_output = st.columns(2)
    
    with col_adv_input:
        st.markdown("### Polyalphabetic Input")
        adv_input = st.text_area("Enter text for polyalphabetic encryption:", 
                                "The five boxing wizards jump quickly.", 
                                height=100)
        
        st.markdown("#### Multiple Keys")
        key1 = st.slider("Key 1:", 1, 25, 3)
        key2 = st.slider("Key 2:", 1, 25, 7)
        key3 = st.slider("Key 3:", 1, 25, 12)
        
        keys = [key1, key2, key3]
        adv_encrypt_button = st.button("Encrypt with Multiple Keys")
    
    with col_adv_output:
        st.markdown("### Polyalphabetic Output")
        
        if adv_encrypt_button and adv_input:
            poly_encrypted = poly_encrypt(adv_input, keys)
            st.text_area("Encrypted text:", poly_encrypted, height=100)
            
            # Show decryption option
            if st.button("Decrypt with Multiple Keys"):
                poly_decrypted = poly_decrypt(poly_encrypted, keys)
                st.text_area("Decrypted text:", poly_decrypted, height=100)
            
            # Explanation of polyalphabetic advantage
            st.markdown("""
            ### Why Polyalphabetic Is Stronger
            
            Using multiple keys in sequence disrupts the frequency patterns that make simple 
            substitution ciphers vulnerable to analysis. In standard substitution:
            
            - Each letter always encrypts to the same ciphertext letter
            - This preserves frequency patterns (e.g., 'E' is most common in English)
            
            With polyalphabetic substitution:
            
            - The same letter can encrypt to different ciphertext letters
            - Frequency analysis becomes much more difficult
            - The encryption is more resistant to basic cryptanalysis
            """)

# Security considerations
st.subheader("Security Considerations")

st.markdown("""
### Strengths

- **Simplicity**: Easy to understand and implement
- **Performance**: Efficient with minimal computational resources
- **Customization**: Key selection allows for personalized security
- **Educational Value**: Demonstrates fundamental encryption concepts

### Limitations

- **Vulnerability to Known-Plaintext Attacks**: If an attacker has both plaintext and ciphertext, the key can be derived
- **Limited Key Space**: With only 25 possible keys for basic version, brute force is feasible
- **Frequency Analysis**: Despite enhancements, patterns may still be detectable with sufficient ciphertext

### Appropriate Use Cases

- **Educational Environments**: Teaching cryptography basics
- **Low-Sensitivity Information**: Quick protection for non-critical data
- **Resource-Constrained Devices**: When computational power is limited
- **Casual Communication**: Personal messages where advanced encryption is unnecessary

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
