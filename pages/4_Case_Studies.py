import streamlit as st
import pandas as pd
from data_visualization import get_encryption_comparison, create_encryption_comparison

# Configure page
st.set_page_config(
    page_title="Case Studies - Cyber Yantra",
    page_icon="🔐",
    layout="wide"
)

# Title
st.title("Case Studies and Real-Life Applications")
st.markdown("## Where Encryption Tools Like Cyber Yantra Are Needed")

# Introduction
st.markdown("""
While advanced encryption standards are essential for high-security applications, 
lightweight encryption tools like Cyber Yantra serve important purposes in various
scenarios. This page explores real-world applications and compares different
encryption techniques.
""")

# Real-world scenarios
st.subheader("Real-World Applications")

scenarios = [
    {
        "title": "Educational Settings",
        "description": """
        **Scenario**: Computer science and cybersecurity courses teaching encryption fundamentals.
        
        **Challenge**: Students need to understand basic encryption concepts before moving to complex algorithms.
        
        **Solution**: Cyber Yantra provides a transparent, step-by-step encryption process that clearly 
        demonstrates substitution ciphers and modular arithmetic in action.
        
        **Outcome**: Students gain practical experience with encryption fundamentals, preparing them for 
        more advanced cryptographic studies.
        """
    },
    {
        "title": "Low-Resource IoT Devices",
        "description": """
        **Scenario**: Small IoT sensors with limited processing power and memory.
        
        **Challenge**: Need to secure basic data transmission without draining limited resources.
        
        **Solution**: Lightweight encryption methods that balance security with performance constraints.
        
        **Outcome**: Devices can transmit data with basic protection against casual interception, while 
        conserving power and computational resources.
        """
    },
    {
        "title": "Rapid Prototyping",
        "description": """
        **Scenario**: Developers building proof-of-concept applications with basic security needs.
        
        **Challenge**: Need a quick-to-implement security layer during development.
        
        **Solution**: Simple encryption methods that can be easily integrated into early prototypes.
        
        **Outcome**: Basic confidentiality during testing phases, with the understanding that 
        production implementations will use more robust encryption standards.
        """
    },
    {
        "title": "Legacy System Integration",
        "description": """
        **Scenario**: Older systems with limited processing capabilities that need to communicate with modern networks.
        
        **Challenge**: Legacy hardware cannot support computation-intensive encryption but requires some protection.
        
        **Solution**: Lightweight encryption that provides basic security without overwhelming outdated hardware.
        
        **Outcome**: Extended useful life of legacy systems with improved security posture compared to unencrypted communication.
        """
    }
]

for scenario in scenarios:
    with st.expander(scenario["title"]):
        st.markdown(scenario["description"])

# Encryption methods comparison
st.subheader("Encryption Methods Comparison")

# Get comparison data from data_visualization module
comparison_df = get_encryption_comparison()

# Display as a table
st.dataframe(comparison_df, use_container_width=True)

# Interactive comparison visualization
st.markdown("### Interactive Comparison")
st.markdown("""
Select encryption methods to compare their characteristics across multiple dimensions:
""")

# Create multi-select for encryption methods
selected_methods = st.multiselect(
    "Select encryption methods to compare:",
    comparison_df['Method'].tolist(),
    default=['Caesar Cipher', 'Cyber Yantra', 'AES-256']
)

if selected_methods:
    # Create radar chart from data_visualization module
    radar_chart = create_encryption_comparison(selected_methods)
    st.plotly_chart(radar_chart, use_container_width=True)
else:
    st.info("Please select at least one encryption method to view the comparison chart.")

# Cyber Yantra vs. Traditional Ciphers
st.subheader("Cyber Yantra vs. Traditional Substitution Ciphers")

comparison_table = {
    "Feature": [
        "Key Generation", 
        "Key Space", 
        "Vulnerability to Frequency Analysis", 
        "Handling of Non-Alphabetic Characters",
        "Computational Efficiency",
        "Implementation Complexity",
        "Educational Value"
    ],
    "Traditional Substitution Cipher": [
        "Static or manual key creation",
        "Limited (typically 25 possible keys for single-alphabet Caesar)",
        "Highly vulnerable",
        "Often ignored or treated inconsistently",
        "Very high (extremely lightweight)",
        "Very low (simple algorithm)",
        "Good for basic concepts"
    ],
    "Cyber Yantra": [
        "Dynamic PRNG-based key generation",
        "Enhanced through session-specific keys",
        "Reduced vulnerability (especially in polyalphabetic version)",
        "Preserved unchanged to maintain formatting",
        "High (slightly more complex than traditional)",
        "Low to moderate (more structured implementation)",
        "Excellent for demonstrating cryptographic principles"
    ]
}

comparison_df = pd.DataFrame(comparison_table)
st.table(comparison_df)

# Simulation scenario
st.subheader("Security Breach Simulation")

st.markdown("""
The following simulation demonstrates how different encryption methods would respond to various attack scenarios.
Choose a scenario to see how Cyber Yantra and other methods would fare:
""")

scenarios = [
    "Brute Force Attack", 
    "Frequency Analysis Attack",
    "Known-Plaintext Attack", 
    "Man-in-the-Middle Attack"
]

selected_scenario = st.selectbox("Select attack scenario:", scenarios)

if selected_scenario == "Brute Force Attack":
    st.markdown("""
    ### Brute Force Attack Scenario
    
    In this attack, the adversary attempts to decrypt the message by trying all possible keys.
    
    **Simulation Results:**
    
    | Encryption Method | Time to Crack | Outcome |
    |-------------------|---------------|---------|
    | Caesar Cipher     | Seconds       | ❌ Easily broken |
    | Cyber Yantra (Basic) | Minutes   | ❌ Vulnerable with computing power |
    | Cyber Yantra (Polyalphabetic) | Hours to days | ⚠️ More resistant but still vulnerable |
    | AES-256          | Billions of years | ✅ Practically impossible |
    
    **Why Cyber Yantra is better than basic Caesar cipher:**
    - Dynamic key generation adds an initial barrier
    - Polyalphabetic version requires testing many more combinations
    - More structured implementation reduces implementation vulnerabilities
    
    **Recommendation:**
    For protection against brute force attacks in critical applications, use industry-standard
    encryption with large key spaces (AES, RSA).
    """)
    
elif selected_scenario == "Frequency Analysis Attack":
    st.markdown("""
    ### Frequency Analysis Attack Scenario
    
    In this attack, the adversary analyzes the frequency of characters in the ciphertext to
    deduce the encryption key based on known language patterns (e.g., 'E' is the most common letter in English).
    
    **Simulation Results:**
    
    | Encryption Method | Vulnerability Level | Outcome |
    |-------------------|---------------------|---------|
    | Caesar Cipher     | Very High           | ❌ Easily broken with sufficient text |
    | Cyber Yantra (Basic) | High             | ❌ Vulnerable with sufficient text |
    | Cyber Yantra (Polyalphabetic) | Medium  | ⚠️ More resistant but not immune |
    | Modern Encryption (AES, etc.) | Very Low | ✅ Not vulnerable to this attack |
    
    **Why Cyber Yantra is better than basic Caesar cipher:**
    - Polyalphabetic version disrupts single-letter frequency patterns
    - Multiple keys create more complex statistical patterns
    - Implementation details can add confusion to the ciphertext
    
    **Recommendation:**
    For protection against frequency analysis in applications requiring confidentiality,
    use modern encryption standards or enhance Cyber Yantra with additional obfuscation techniques.
    """)
    
elif selected_scenario == "Known-Plaintext Attack":
    st.markdown("""
    ### Known-Plaintext Attack Scenario
    
    In this attack, the adversary has access to both the plaintext and its encrypted version,
    allowing them to determine the encryption key.
    
    **Simulation Results:**
    
    | Encryption Method | Vulnerability Level | Outcome |
    |-------------------|---------------------|---------|
    | Caesar Cipher     | Very High           | ❌ Trivially broken |
    | Cyber Yantra (Basic) | High             | ❌ Easily broken |
    | Cyber Yantra (Polyalphabetic) | Medium  | ⚠️ More complex but still vulnerable |
    | Modern Encryption (AES, etc.) | Low      | ✅ Resistant to basic known-plaintext attacks |
    
    **Why Cyber Yantra is better than basic Caesar cipher:**
    - Polyalphabetic version requires more plaintext-ciphertext pairs
    - Session-specific keys limit the usefulness of past known plaintexts
    
    **Recommendation:**
    For applications where adversaries might have access to plaintext-ciphertext pairs,
    use modern encryption standards with key derivation functions and initialization vectors.
    """)
    
elif selected_scenario == "Man-in-the-Middle Attack":
    st.markdown("""
    ### Man-in-the-Middle Attack Scenario
    
    In this attack, the adversary intercepts communications between parties and may
    alter messages or inject new ones.
    
    **Simulation Results:**
    
    | Encryption Method | Protection Level | Outcome |
    |-------------------|------------------|---------|
    | Caesar Cipher     | Very Low         | ❌ No protection against interception or modification |
    | Cyber Yantra (Basic) | Low           | ❌ Limited protection against casual interception |
    | Cyber Yantra (Enhanced) | Low to Medium | ⚠️ Better but still vulnerable to sophisticated attacks |
    | TLS/SSL with Modern Encryption | High | ✅ Strong protection with authentication |
    
    **Why Cyber Yantra is better than basic Caesar cipher:**
    - More complex implementation can include integrity checks
    - Dynamic key generation adds a layer of security
    
    **Recommendation:**
    For protection against MITM attacks, combine encryption with digital signatures,
    message authentication codes, and secure key exchange protocols.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <small>
        These case studies and comparisons are for educational purposes.<br>
        For production systems, consult with cybersecurity professionals to determine appropriate encryption solutions.
    </small>
</div>
""", unsafe_allow_html=True)
