import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go

# Common cyber threats and their frequencies (based on common industry data)
def get_cyber_threats_data():
    """Return a DataFrame of common cyber threats and their frequencies"""
    threats = {
        'Threat': [
            'Phishing', 'Malware', 'Ransomware', 'Data Breach', 
            'Man-in-the-Middle', 'DDoS', 'SQL Injection', 
            'Zero-day Exploit', 'Password Attack', 'Social Engineering'
        ],
        'Frequency (%)': [
            32, 28, 21, 19, 14, 12, 11, 9, 24, 31
        ]
    }
    return pd.DataFrame(threats)

# Major cybersecurity breaches timeline
def get_breach_timeline():
    """Return a DataFrame of major cybersecurity breaches"""
    breaches = {
        'Year': [2013, 2014, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Incident': [
            'Yahoo', 'eBay', 'LinkedIn', 'Equifax', 
            'Marriott', 'Capital One', 'SolarWinds', 
            'Colonial Pipeline', 'Log4j', 'Microsoft Exchange'
        ],
        'Impact (Million Users)': [3000, 145, 165, 147, 500, 106, 18, 5, 200, 60],
        'Description': [
            'Data breach affecting all 3 billion accounts',
            'Breach exposed names, addresses, DOBs, and passwords of 145 million users',
            'Hackers stole 165 million user records',
            'Credit bureau breach exposed personal data of 147 million customers',
            'Hotel chain breach exposed personal info of 500 million guests',
            'Credit card application data of 106 million customers was exposed',
            'Supply chain attack affected thousands of organizations',
            'Ransomware attack on fuel pipeline operator',
            'Critical vulnerability in widely used logging library',
            'Zero-day vulnerabilities allowed access to email servers'
        ]
    }
    return pd.DataFrame(breaches)

# Encryption methods comparison
def get_encryption_comparison():
    """Return a DataFrame comparing different encryption methods"""
    comparison = {
        'Method': [
            'Caesar Cipher', 'Cyber Yantra', 'AES-128', 
            'AES-256', 'RSA-2048', 'Triple DES', 'Blowfish'
        ],
        'Key Size (bits)': [
            8, 128, 128, 256, 2048, 168, 448
        ],
        'Security Level': [
            'Very Low', 'Basic', 'High', 'Very High', 'Very High', 'Medium', 'High'
        ],
        'Speed': [
            'Very Fast', 'Fast', 'Fast', 'Fast', 'Slow', 'Slow', 'Fast'
        ],
        'Complexity': [
            'Very Low', 'Low', 'Medium', 'Medium', 'High', 'Medium', 'Medium'
        ]
    }
    return pd.DataFrame(comparison)

# Function to create cybersecurity word cloud
def generate_wordcloud():
    """Generate a word cloud of cybersecurity terms"""
    words = """
    Encryption Decryption Cipher Cybersecurity InfoSec Cryptography
    Vulnerability Threat Malware Phishing Authentication Authorization
    Firewall Virus Trojan Ransomware Spyware Botnet DDoS Breach
    Password Hashing Salting TLS SSL VPN Proxy Privacy GDPR
    Compliance Penetration Identity Biometrics MFA 2FA OTP Zero-trust
    Blockchain Security Cryptanalysis Algorithm Protocol Backdoor
    Keylogger Packet Exploit Sandbox Honeypot IDS IPS Forensics
    Antivirus Whitelist Blacklist Patch Update Cybercrime Hacker
    Plaintext Ciphertext Key Public-key Private-key Asymmetric Symmetric
    """
    
    wc = WordCloud(
        background_color='white',
        width=800,
        height=400,
        max_words=100,
        colormap='viridis',
        contour_width=1
    ).generate(words)
    
    return wc

# Create threat frequency chart
def create_threat_chart():
    """Create a bar chart of cyber threat frequencies"""
    threats_df = get_cyber_threats_data()
    
    fig = px.bar(
        threats_df, 
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
    
    return fig

# Create breach timeline visualization
def create_breach_timeline():
    """Create an interactive timeline of major data breaches"""
    breaches_df = get_breach_timeline()
    
    fig = px.scatter(
        breaches_df, 
        x='Year', 
        y='Impact (Million Users)',
        size='Impact (Million Users)',
        color='Incident',
        hover_name='Incident',
        hover_data=['Description'],
        title='Timeline of Major Cybersecurity Breaches',
        size_max=50
    )
    
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Impact (Million Users Affected)',
        xaxis=dict(tickmode='linear', dtick=1)
    )
    
    return fig

# Create encryption comparison visualization
def create_encryption_comparison(selected_methods=None):
    """Create a radar chart comparing encryption methods"""
    comp_df = get_encryption_comparison()
    
    if selected_methods:
        comp_df = comp_df[comp_df['Method'].isin(selected_methods)]
    
    # Convert categorical values to numerical for radar chart
    security_map = {'Very Low': 1, 'Low': 2, 'Basic': 3, 'Medium': 4, 'High': 5, 'Very High': 6}
    speed_map = {'Very Slow': 1, 'Slow': 2, 'Medium': 3, 'Fast': 4, 'Very Fast': 5}
    complexity_map = {'Very Low': 1, 'Low': 2, 'Medium': 3, 'High': 4, 'Very High': 5}
    
    comp_df['Security_Score'] = comp_df['Security Level'].map(security_map)
    comp_df['Speed_Score'] = comp_df['Speed'].map(speed_map)
    comp_df['Complexity_Score'] = comp_df['Complexity'].map(complexity_map)
    
    # Normalize key size for better visualization
    max_key = comp_df['Key Size (bits)'].max()
    comp_df['Key_Size_Normalized'] = comp_df['Key Size (bits)'] / max_key * 5
    
    # Create radar chart
    categories = ['Security', 'Speed', 'Complexity', 'Key Size']
    
    fig = go.Figure()
    
    for i, row in comp_df.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=[row['Security_Score'], row['Speed_Score'], 
               row['Complexity_Score'], row['Key_Size_Normalized']],
            theta=categories,
            fill='toself',
            name=row['Method']
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 6]
            )
        ),
        title="Encryption Methods Comparison",
        showlegend=True
    )
    
    return fig
