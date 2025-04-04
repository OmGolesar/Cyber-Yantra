import streamlit as st

# Configure page
st.set_page_config(
    page_title="Research Overview - Cyber Yantra",
    page_icon="🔐",
    layout="wide"
)

# Title
st.title("Research Overview")
st.markdown("## Cyber Yantra: A Substitution Cipher-Based Encryption Tool")

# Research Objectives
st.markdown("""
### Research Objectives

The Cyber Yantra research project aims to:

1. **Develop a lightweight encryption tool** that balances security with computational efficiency
2. **Enhance traditional substitution ciphers** by integrating dynamic key-based substitutions and modular arithmetic
3. **Address the limitations** of classical substitution methods, particularly vulnerability to frequency analysis
4. **Create an accessible encryption solution** for educational environments and low-resource settings
5. **Bridge the gap** between classical cryptographic principles and modern security requirements
""")

# Key Innovations
st.markdown("""
### Key Innovations

The research introduces several innovations to traditional substitution ciphers:

- **Dynamic Key Generation**: Using pseudo-random number generators (PRNG) to produce unique keys for each session
- **Modular Arithmetic Operations**: Applying robust mathematical principles to enhance encryption strength
- **Cross-Platform Implementation**: Designing the solution to work across different computing environments
- **Balanced Security Approach**: Offering stronger protection than classical ciphers while maintaining simplicity
""")

# Methodology Summary
st.subheader("Methodology")
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    #### Problem Addressed
    
    Modern digital communication requires protecting sensitive information, but classical substitution 
    ciphers are vulnerable to frequency analysis and brute-force attacks. In resource-constrained 
    environments, there's a need for lightweight yet secure encryption methods.
    
    #### Implementation Approach
    
    Cyber Yantra is built using high-level programming languages (Python, JavaScript) ensuring cross-platform
    compatibility. The web-based interface facilitates usage in educational and low-resource environments.
    """)

with col2:
    st.markdown("""
    #### Core Algorithm Components
    
    1. **Key Generation**: PRNG produces dynamic keys for each encryption session
    2. **Character Substitution**:
       - Validates if character is alphabetic
       - Calculates position in alphabet
       - Applies shift operation using modular arithmetic
       - Implements the formula: `new_index = (current_index + key) mod 26`
    3. **Decryption Process**:
       - Reverses the transformation using the same key
       - Formula: `original_index = (current_index - key + 26) mod 26`
    """)

# Research Context
st.subheader("Research Context")
st.markdown("""
The development of Cyber Yantra builds upon existing research in lightweight cryptography:

1. **Al‑Salami (2019)** introduced randomized key matrices to fortify classical substitution ciphers
2. **Alabaichi et al. (2020)** explored polyalphabetic substitution strategies for IoT applications
3. **Smith and Doe (2022)** proposed hybrid encryption models combining classical techniques with AES-inspired mechanisms

Cyber Yantra integrates insights from these studies to create a balanced encryption approach that mitigates
vulnerabilities while maintaining simplicity and performance.
""")

# Significance
st.markdown("""
### Significance in Modern Cybersecurity

While advanced encryption standards like AES and RSA dominate modern secure communication, 
Cyber Yantra serves important purposes:

- **Educational Value**: Helps learners understand fundamental encryption principles
- **Resource Efficiency**: Suitable for environments with limited computational resources
- **Balanced Approach**: Bridges simple classical methods and complex modern standards
- **Practical Applications**: Useful for basic confidentiality needs in non-critical scenarios

The tool demonstrates how classical cryptographic principles can be enhanced to meet contemporary 
security challenges while maintaining accessibility.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <small>
        Based on research by Tanmay S Dikshit, Om Raju Golesar, Niraj Digambar Shinde, Kishor M Mahale and Ratan D Deokar.<br>
        This page summarizes the research paper "Cyber Yantra: A Substitution Cipher-Based Encryption Tool for Secure Digital Communication"
    </small>
</div>
""", unsafe_allow_html=True)
