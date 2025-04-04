import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from data_visualization import generate_wordcloud, create_breach_timeline, get_breach_timeline
from wordcloud import WordCloud
import numpy as np

# Configure page
st.set_page_config(
    page_title="Interactive Visualizations - Cyber Yantra",
    page_icon="🔐",
    layout="wide"
)

# Title
st.title("Interactive Data Visualizations")
st.markdown("## Exploring Cybersecurity Trends and Concepts")

# Introduction
st.markdown("""
Data visualizations help us understand complex cybersecurity concepts and trends.
This page provides interactive visualizations related to encryption, data breaches,
and cyber threats.
""")

# Timeline of major breaches
st.subheader("Timeline of Major Cybersecurity Breaches")
st.markdown("""
The following timeline shows significant data breaches over the past decade.
These incidents highlight the critical importance of proper encryption and security measures.
""")

# Get and display the breach timeline from data_visualization module
breach_timeline = create_breach_timeline()
st.plotly_chart(breach_timeline, use_container_width=True)

# Add interactivity - details on selected breach
breaches_df = get_breach_timeline()
selected_breach = st.selectbox(
    "Select a breach for more details:",
    breaches_df['Incident'].tolist()
)

# Display details for the selected breach
breach_details = breaches_df[breaches_df['Incident'] == selected_breach].iloc[0]
st.markdown(f"""
### {breach_details['Incident']} ({breach_details['Year']})

**Impact**: Affected approximately {breach_details['Impact (Million Users)']} million users

**Description**: {breach_details['Description']}

**Key Lesson**: {
    "Implement regular security audits and breach detection systems." if selected_breach == "Yahoo" else
    "Promptly apply security patches for known vulnerabilities." if selected_breach == "Equifax" else
    "Use strong authentication including MFA for all access points." if selected_breach == "Colonial Pipeline" else
    "Implement comprehensive security measures including encryption." if selected_breach == "Marriott" else
    "Ensure proper monitoring of cloud resources and access controls." if selected_breach == "Capital One" else
    "Verify supply chain security and monitor for suspicious activities." if selected_breach == "SolarWinds" else
    "Address vulnerabilities quickly, especially in widely used libraries." if selected_breach == "Log4j" else
    "Keep systems updated and implement defense-in-depth strategies."
}

**How Encryption Could Have Helped**: {
    "Proper encryption of user data would have made the stolen information unusable to attackers." if selected_breach in ["Yahoo", "eBay", "LinkedIn", "Equifax", "Marriott", "Capital One"] else
    "End-to-end encryption could have prevented attackers from accessing sensitive communications." if selected_breach == "SolarWinds" else
    "Encrypted backups and segmentation could have limited the impact of the ransomware attack." if selected_breach == "Colonial Pipeline" else
    "Encrypted communications could have reduced the attack surface for exploitation." if selected_breach in ["Log4j", "Microsoft Exchange"] else
    "Strong encryption of sensitive data could have mitigated the impact of the breach."
}
""")

# Cybersecurity word cloud
st.subheader("Cybersecurity Concepts Word Cloud")
st.markdown("""
This word cloud highlights important terms and concepts in the field of cybersecurity and encryption.
The size of each word indicates its relative importance or frequency in cybersecurity discussions.
""")

# Generate word cloud using function from data_visualization module
wc = generate_wordcloud()

# Display the word cloud
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Interactive encryption strength visualization
st.subheader("Encryption Strength Visualization")
st.markdown("""
This interactive visualization demonstrates the relative strength of different encryption methods
based on their key size and resistance to various attack methods.
""")

# Create data for the visualization
encryption_data = {
    'Method': [
        'Caesar Cipher (8-bit)', 'Cyber Yantra Basic (128-bit)', 
        'Cyber Yantra Enhanced (256-bit)', 'DES (56-bit)', 
        'Triple DES (168-bit)', 'AES-128', 'AES-256', 'RSA-2048'
    ],
    'Key Size (bits)': [8, 128, 256, 56, 168, 128, 256, 2048],
    'Time to Brute Force': [
        'Milliseconds', 'Hours', 'Days', 
        'Hours', 'Years', 'Billions of years', 
        'Trillions of years', 'Quintillions of years'
    ],
    'Numeric Strength': [1, 25, 40, 20, 60, 90, 95, 99]  # Arbitrary scale for visualization
}

strength_df = pd.DataFrame(encryption_data)

# Create interactive bar chart
fig = px.bar(
    strength_df, 
    x='Method', 
    y='Numeric Strength',
    title='Relative Encryption Strength Comparison',
    hover_data=['Key Size (bits)', 'Time to Brute Force'],
    color='Numeric Strength',
    color_continuous_scale='viridis',
    labels={'Numeric Strength': 'Strength Score (0-100)'}
)

fig.update_layout(xaxis_title='Encryption Method', yaxis_title='Strength Score')
st.plotly_chart(fig, use_container_width=True)

# Interactive data exploration
st.subheader("Explore Encryption Metrics")

# Create some sample data on encryption performance
perf_data = {
    'Encryption Method': np.repeat(['Caesar Cipher', 'Cyber Yantra', 'AES-128', 'AES-256', 'RSA-2048'], 5),
    'Data Size (KB)': np.tile([10, 100, 1000, 10000, 100000], 5),
    'Encryption Time (ms)': [
        # Caesar Cipher times
        0.1, 0.5, 5, 50, 500,
        # Cyber Yantra times
        0.2, 1, 10, 100, 1000,
        # AES-128 times
        0.5, 3, 30, 300, 3000,
        # AES-256 times
        0.6, 4, 40, 400, 4000,
        # RSA-2048 times
        10, 100, 1000, 10000, 100000
    ]
}

perf_df = pd.DataFrame(perf_data)

# Add log-scaled columns for better visualization
perf_df['Log Data Size'] = np.log10(perf_df['Data Size (KB)'])
perf_df['Log Encryption Time'] = np.log10(perf_df['Encryption Time (ms)'])

# Let user select visualization type
viz_type = st.selectbox(
    "Select visualization type:",
    ["Performance by Data Size", "Method Comparison", "3D Visualization"]
)

if viz_type == "Performance by Data Size":
    # Line chart showing performance scaling with data size
    fig = px.line(
        perf_df, 
        x='Data Size (KB)', 
        y='Encryption Time (ms)',
        color='Encryption Method',
        log_x=True, 
        log_y=True,
        title='Encryption Performance Scaling by Data Size',
        markers=True
    )
    
    fig.update_layout(
        xaxis_title='Data Size (KB, log scale)',
        yaxis_title='Encryption Time (ms, log scale)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Observation**: This logarithmic plot shows how encryption time scales with data size for different methods.
    Notice that simpler methods like Caesar Cipher and Cyber Yantra are more efficient for small data sizes,
    but all methods show linear scaling (parallel lines on log-log plot) as data size increases.
    """)
    
elif viz_type == "Method Comparison":
    # Specific data size to compare
    size_options = [10, 100, 1000, 10000, 100000]
    selected_size = st.select_slider(
        "Select data size (KB) for comparison:",
        options=size_options
    )
    
    # Filter data for selected size
    filtered_df = perf_df[perf_df['Data Size (KB)'] == selected_size]
    
    # Bar chart comparing methods
    fig = px.bar(
        filtered_df,
        x='Encryption Method',
        y='Encryption Time (ms)',
        color='Encryption Method',
        title=f'Encryption Time Comparison for {selected_size} KB Data',
        log_y=True
    )
    
    fig.update_layout(
        xaxis_title='Encryption Method',
        yaxis_title='Encryption Time (ms, log scale)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    **Observation**: For {selected_size} KB of data, this comparison shows the relative performance
    of different encryption methods. Simpler substitution ciphers like Caesar and Cyber Yantra
    are faster, while more secure methods like RSA require significantly more processing time.
    """)
    
else:  # 3D Visualization
    # 3D surface plot
    fig = go.Figure(data=[
        go.Surface(
            z=perf_df.pivot(
                index='Encryption Method', 
                columns='Data Size (KB)', 
                values='Encryption Time (ms)'
            ).values,
            x=[10, 100, 1000, 10000, 100000],  # Data sizes from perf_data
            y=['Caesar Cipher', 'Cyber Yantra', 'AES-128', 'AES-256', 'RSA-2048'],
            colorscale='Viridis'
        )
    ])
    
    fig.update_layout(
        title='3D Encryption Performance Surface',
        scene=dict(
            xaxis_title='Data Size (KB)',
            yaxis_title='Encryption Method',
            zaxis_title='Encryption Time (ms)'
        ),
        width=800,
        height=700
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Observation**: This 3D surface visualizes the relationship between encryption method,
    data size, and processing time. The surface's slope indicates how quickly performance
    degrades as data size increases for each method.
    """)

# Interactive frequency analysis demonstration
st.subheader("Frequency Analysis Vulnerability Demonstration")
st.markdown("""
This interactive tool demonstrates why simple substitution ciphers (including basic versions of Cyber Yantra) 
are vulnerable to frequency analysis attacks. Enter text to see character frequencies in both 
plaintext and ciphertext.
""")

# Text input for frequency analysis
freq_text = st.text_area(
    "Enter text to analyze:",
    "The quick brown fox jumps over the lazy dog. This pangram contains all letters of the English alphabet.",
    height=100
)

if freq_text:
    # Calculate character frequencies
    freq_counts = {}
    alpha_only = ''.join(c.lower() for c in freq_text if c.isalpha())
    
    for char in alpha_only:
        if char in freq_counts:
            freq_counts[char] += 1
        else:
            freq_counts[char] = 1
    
    # Convert to percentages
    total_chars = len(alpha_only)
    freq_percentages = {char: (count / total_chars) * 100 for char, count in freq_counts.items()}
    
    # Sort by character
    sorted_freqs = dict(sorted(freq_percentages.items()))
    
    # Create frequency bar chart
    fig = px.bar(
        x=list(sorted_freqs.keys()),
        y=list(sorted_freqs.values()),
        title='Character Frequency Distribution',
        labels={'x': 'Character', 'y': 'Frequency (%)'}
    )
    
    fig.update_layout(xaxis_title='Character', yaxis_title='Frequency (%)')
    st.plotly_chart(fig, use_container_width=True)
    
    # Show typical English frequency distribution for comparison
    st.markdown("""
    ### English Language Letter Frequency
    
    For comparison, here is the standard frequency distribution of letters in English text:
    
    E (12.7%), T (9.1%), A (8.2%), O (7.5%), I (7.0%), N (6.7%), S (6.3%), H (6.1%), 
    R (6.0%), D (4.3%), L (4.0%), U (2.8%), C (2.8%), M (2.4%), W (2.4%), F (2.2%), 
    G (2.0%), Y (2.0%), P (1.9%), B (1.5%), V (1.0%), K (0.8%), J (0.2%), X (0.2%), 
    Q (0.1%), Z (0.1%)
    
    **Why This Matters**: In a simple substitution cipher, these frequency patterns remain intact,
    just shifted to different letters. Analysts can identify the most frequent letters in the 
    ciphertext and match them to expected frequencies (like E, T, A) to break the cipher.
    
    **How Cyber Yantra Improves This**: The polyalphabetic version of Cyber Yantra disrupts these
    frequency patterns by using multiple keys, making frequency analysis more difficult.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <small>
        Data visualizations are for educational purposes.<br>
        Performance metrics are approximate and may vary based on implementation and hardware.
    </small>
</div>
""", unsafe_allow_html=True)
