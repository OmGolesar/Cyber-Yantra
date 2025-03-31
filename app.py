import streamlit as st
import base64
from cyber_yantra import encrypt_text, decrypt_text

# Page configuration
st.set_page_config(
    page_title="Cyber Yantra - Encryption Tool",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and introduction
st.title("🔐 Cyber Yantra")
st.subheader("A Substitution Cipher-Based Encryption Tool for Secure Digital Communication")

# Create columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## Welcome to Cyber Yantra
    
    In the digital age, safeguarding sensitive information is paramount. Cyber Yantra is a 
    lightweight encryption tool employing a substitution cipher mechanism for basic text 
    confidentiality.
    
    This application demonstrates the concepts, research, and practical applications of the 
    Cyber Yantra encryption tool as described in the research paper by Tanmay S Dikshit, 
    Om Raju Golesar, Niraj Digambar Shinde, and Kishor M Mahale.
    
    ### What is Cyber Yantra?
    
    Cyber Yantra bridges classical and contemporary cryptographic approaches by leveraging 
    dynamic key-based substitutions combined with modular arithmetic. It offers a balanced 
    solution that is both accessible and secure, making it particularly suitable for 
    educational purposes and resource-constrained environments.
    """)

with col2:
    # Display a cybersecurity-related image (using a placeholder icon)
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <i class="material-icons" style="font-size: 150px; color: #0066cc;">lock</i>
        <p>Secure your communications with Cyber Yantra</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Try the encryption tool directly
    st.markdown("### Try it now!")
    demo_text = st.text_input("Enter text to encrypt:", "Hello, Cyber Yantra!")
    key = st.slider("Select encryption key (1-25):", 1, 25, 7)
    
    if demo_text:
        encrypted = encrypt_text(demo_text, key)
        st.success(f"Encrypted: **{encrypted}**")
        
        if st.button("Decrypt"):
            decrypted = decrypt_text(encrypted, key)
            st.info(f"Decrypted: **{decrypted}**")

# Download research paper option
st.sidebar.title("Navigation")
st.sidebar.info("""
Use the navigation menu above to explore different sections:
1. Home (current page)
2. Research Overview
3. Importance of Secure Communication
4. Cyber Yantra Encryption Mechanism
5. Case Studies and Real-Life Applications
6. Interactive Data Visualizations
7. Conclusion & Future Scope
""")

# Load paper content
with open("assets/cyber_yantra_paper.txt", "r") as f:
    paper_content = f.read()

def get_download_link(text, filename, link_text):
    """Generate a download link for text content"""
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{link_text}</a>'
    return href

st.sidebar.markdown("### Research Paper")
st.sidebar.markdown(get_download_link(paper_content, "Cyber_Yantra_Research_Paper.txt", "Download Research Paper"), unsafe_allow_html=True)
st.sidebar.markdown("---")

# Footer with credits
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <small>
        Created based on the research by Tanmay S Dikshit, Om Raju Golesar, Niraj Digambar Shinde, and Kishor M Mahale.<br>
        This application is for educational purposes only.
    </small>
</div>
""", unsafe_allow_html=True)
