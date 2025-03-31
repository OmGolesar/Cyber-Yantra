import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_visualization import get_cyber_threats_data

# Configure page
st.set_page_config(
    page_title="Secure Communication - Cyber Yantra",
    page_icon="🔐",
    layout="wide"
)

# Title
st.title("The Importance of Secure Communication")
st.markdown("## Why Encryption Matters in the Digital Age")

# Introduction
st.markdown("""
In today's interconnected world, data is constantly being transmitted across various networks and platforms.
From personal messages and financial transactions to business communications and healthcare records,
sensitive information is vulnerable to interception and exploitation without proper security measures.
""")

# Key Statistics
st.subheader("Cybersecurity: By the Numbers")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Average Cost of a Data Breach (2023)",
        value="$4.45M",
        delta="+15% from 2020",
        delta_color="inverse"
    )
    st.caption("Source: IBM Cost of a Data Breach Report")

with col2:
    st.metric(
        label="Cybercrime Costs Projected (2025)",
        value="$10.5T",
        delta="Annual increase of 15%",
        delta_color="inverse"
    )
    st.caption("Source: Cybersecurity Ventures")

with col3:
    st.metric(
        label="% of Breaches Involving Human Element",
        value="82%",
        delta="+3% from previous year",
        delta_color="inverse"
    )
    st.caption("Source: Verizon Data Breach Investigations Report")

# Common Cyber Threats
st.subheader("Common Cyber Threats to Communication")

# Get threat data from data_visualization module
threat_data = get_cyber_threats_data()

# Create bar chart
fig = px.bar(
    threat_data, 
    x='Threat', 
    y='Frequency (%)',
    title='Common Cyber Threats (Frequency)',
    color='Frequency (%)',
    color_continuous_scale='Viridis'
)

fig.update_layout(
    xaxis_title='Threat Type',
    yaxis_title='Frequency (%)',
    xaxis={'categoryorder':'total descending'}
)

st.plotly_chart(fig, use_container_width=True)

# Real-world case studies
st.subheader("Case Studies: When Communication Security Fails")

case_studies = [
    {
        "title": "Yahoo Data Breach (2013-2014)",
        "impact": "3 billion user accounts compromised",
        "description": "One of the largest breaches in history affected all Yahoo user accounts. Stolen information included names, email addresses, phone numbers, and hashed passwords. The breach was discovered years after it occurred, highlighting the need for better security monitoring."
    },
    {
        "title": "Equifax Breach (2017)",
        "impact": "147 million Americans affected",
        "description": "Hackers exploited a vulnerability in Equifax's website to access sensitive personal and financial information including Social Security numbers, birth dates, addresses, and credit card numbers. The breach occurred due to failure to patch a known security flaw."
    },
    {
        "title": "Colonial Pipeline Ransomware Attack (2021)",
        "impact": "Fuel shortages across Eastern US",
        "description": "A ransomware attack forced the company to shut down its 5,500-mile pipeline that carries 45% of the East Coast's fuel supplies. The attack was possible due to a compromised password to an obsolete VPN account that lacked multi-factor authentication."
    }
]

for i, case in enumerate(case_studies):
    with st.expander(f"{case['title']} - {case['impact']}"):
        st.markdown(case['description'])
        st.markdown("---")
        if i == 0:
            st.markdown("**Lesson**: Regular security audits and timely breach detection are essential.")
        elif i == 1:
            st.markdown("**Lesson**: Prompt application of security patches is crucial for vulnerability management.")
        else:
            st.markdown("**Lesson**: Strong authentication methods including MFA are necessary, even for legacy systems.")

# Encryption's role
st.subheader("How Encryption Protects Communication")

st.markdown("""
Encryption serves as a fundamental safeguard in digital communications by:

1. **Confidentiality**: Ensuring that only authorized recipients can access the information
2. **Integrity**: Verifying that messages haven't been altered during transmission
3. **Authentication**: Confirming the identity of the sender
4. **Non-repudiation**: Preventing the sender from denying they sent the message

Even if data is intercepted during transmission, properly encrypted information remains unreadable and unusable 
to unauthorized parties.
""")

# Encryption process visualization
st.markdown("### Simplified Encryption Process")

# Create a simple flowchart of encryption process
encryption_process = {
    'Step': ['Original Message', 'Apply Encryption Algorithm', 'Encrypted Message', 
             'Transmission', 'Apply Decryption Algorithm', 'Received Message'],
    'Description': [
        'Plaintext readable by anyone',
        'Use encryption key to scramble the message',
        'Ciphertext unreadable without the key',
        'Message travels through potentially insecure channels',
        'Use decryption key to unscramble the message',
        'Original plaintext recovered by authorized recipient'
    ],
    'Position': [1, 2, 3, 4, 5, 6]  # For ordering the steps
}

df_process = pd.DataFrame(encryption_process)

# Create the visualization
fig = go.Figure()

for i, row in df_process.iterrows():
    fig.add_trace(go.Scatter(
        x=[row['Position']],
        y=[0],
        mode='markers+text',
        marker=dict(size=30, color='#0066cc'),
        text=row['Step'],
        textposition='bottom center',
        hoverinfo='text',
        hovertext=row['Description'],
        name=row['Step']
    ))

# Add arrows connecting the steps
for i in range(len(df_process) - 1):
    fig.add_shape(
        type="line",
        x0=df_process.iloc[i]['Position'],
        y0=0,
        x1=df_process.iloc[i+1]['Position'],
        y1=0,
        line=dict(color="#0066cc", width=2, dash="solid"),
        layer="below"
    )

fig.update_layout(
    title="The Encryption Process Flow",
    xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
    yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
    showlegend=False,
    height=300,
    margin=dict(l=20, r=20, t=40, b=20),
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)

# Call to action / Conclusion
st.markdown("""
### Secure Communication is Not Optional

In a world where data breaches and cyber attacks are increasingly common, encryption is not just 
a technical feature but a necessity for:

- **Individuals**: Protecting personal information, financial data, and private communications
- **Businesses**: Safeguarding intellectual property, customer data, and business communications
- **Governments**: Securing classified information and critical infrastructure
- **Healthcare**: Ensuring patient confidentiality and compliance with regulations

Tools like Cyber Yantra aim to make encryption more accessible, helping to protect communications 
from unauthorized access and maintaining privacy in our increasingly digital lives.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <small>
        Data sources include IBM Security, Cybersecurity Ventures, and Verizon DBIR.<br>
        This information is provided for educational purposes only.
    </small>
</div>
""", unsafe_allow_html=True)
