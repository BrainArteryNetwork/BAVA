"""
    About Us page for the Brain Artery Network Visualization and Analysis platform.
    Displays team information and mission statement.
"""
import streamlit as st
import os
from pathlib import Path

def get_asset_path(filename):
    """Get the full path for an asset file."""
    current_dir = Path(__file__).parent.parent
    root_dir = current_dir.parent
    return os.path.join(root_dir, 'static', 'images', filename)

def set_page_style():
    """Set custom CSS styles for the page."""
    st.markdown("""
        <style>
        /* Main background and text colors */
        .stApp {
            background: linear-gradient(to bottom, rgba(10, 25, 47, 0.95), rgba(23, 42, 70, 0.95));
            color: white;
        }
        
        /* Mission section styling */
        .mission-section {
            background: rgba(255, 206, 155, 0.1);
            padding: 40px;
            border-radius: 20px;
            margin: 40px 0;
            backdrop-filter: blur(10px);
        }
        
        .mission-title {
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 30px;
            color: #ffa500;
        }
        
        .mission-text {
            font-size: 18px;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.9);
        }
        
        /* Team section styling */
        .team-section {
            margin-top: 60px;
        }
        
        .team-title {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 40px;
            color: #ffa500;
            border-bottom: 2px solid #ffa500;
            padding-bottom: 10px;
        }
        
        .team-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            justify-content: center;
        }
        
        .team-member {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            width: 300px;
            text-align: center;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: transform 0.3s ease;
        }
        
        .team-member:hover {
            transform: translateY(-5px);
        }
        
        .member-image {
            width: 200px;
            height: 200px;
            border-radius: 15px;
            margin-bottom: 20px;
            object-fit: cover;
            border: 3px solid #ffa500;
        }
        
        .member-name {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #ffa500;
        }
        
        .member-title {
            font-size: 16px;
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 15px;
        }
        
        .member-bio {
            font-size: 14px;
            color: rgba(255, 255, 255, 0.8);
            line-height: 1.5;
        }
        </style>
    """, unsafe_allow_html=True)

def mission_section():
    """Display the mission statement section."""
    st.markdown("""
        <div class="mission-section">
            <div class="mission-title">About BAVA Platform</div>
            <div class="mission-text">
                The Brain Artery Visualization and Analysis (BAVA) platform is a cutting-edge initiative 
                designed to revolutionize neurovascular research. Our platform provides researchers with:
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Platform Features
    st.markdown("""
        * Advanced 3D visualization tools for brain artery networks extracted from MRA imaging
        * Standardized datasets integrating multimodal data including demographic and clinical information
        * Graph Neural Network (GNN)-based analytical pipeline for comprehensive network analysis
        * Tools for cross-sectional studies across diverse populations
    """)

    # What You Can Do section
    st.markdown("<div style='font-size: 24px; color: #ffa500; margin-top: 30px;'>What You Can Do</div>", unsafe_allow_html=True)
    st.markdown("""
        * Explore harmonized brain artery network datasets
        * Analyze complex 3D structures using our advanced visualization tools
        * Conduct reproducible research across diverse populations
        * Contribute to expanding our understanding of neurovascular health
    """)

    # Research Goals section
    st.markdown("<div style='font-size: 24px; color: #ffa500; margin-top: 30px;'>Research Goals</div>", unsafe_allow_html=True)
    st.markdown("""
        * Establish a harmonized, multimodal dataset for comprehensive brain artery network analysis
        * Develop innovative GNN-based analytical methods for predicting neurovascular health outcomes
        * Enable early detection of cerebrovascular risks through advanced biomarker identification
        * Foster collaboration within the neurovascular research community
    """)

def team_section():
    """Display the team members section."""
    st.markdown('<div class="team-title">Our Team</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="team-member">
                <img src="https://raw.githubusercontent.com/BrainArteryNetwork/BAVA/main/bava/static/images/team_member1.jpg" alt="Team Member 1" class="member-image">
                <div class="member-name">Dr. Sarah Chen</div>
                <div class="member-title">Lead Researcher (UW Medicine)</div>
                <div class="member-bio">
                    Specializing in neurovascular imaging and analysis, with over 10 years of experience 
                    in clinical research and machine learning applications in healthcare.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="team-member">
                <img src="https://raw.githubusercontent.com/BrainArteryNetwork/BAVA/main/bava/static/images/team_member2.jpg" alt="Team Member 2" class="member-image">
                <div class="member-name">Dr. Michael Rodriguez</div>
                <div class="member-title">Technical Lead (UW CSE)</div>
                <div class="member-bio">
                    Expert in medical image processing and software development, leading the technical 
                    implementation of BAVA's visualization and analysis tools.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="team-member">
                <img src="https://raw.githubusercontent.com/BrainArteryNetwork/BAVA/main/bava/static/images/team_member3.jpg" alt="Team Member 3" class="member-image">
                <div class="member-name">Dr. James Wilson</div>
                <div class="member-title">Research Director (UW Medicine)</div>
                <div class="member-bio">
                    Leading research initiatives in neurovascular health, with a focus on developing 
                    novel approaches to understanding brain artery networks.
                </div>
            </div>
        """, unsafe_allow_html=True)

def achievements_section():
    """Display the achievements section."""
    st.markdown("""
        <div class="mission-section" style="margin-top: 60px;">
            <div class="mission-title">Current Progress</div>
            <div class="mission-text">
                <div style="margin: 20px 0;">
                    • 🔬 Analyzed over 500 brain scans using advanced algorithms<br>
                    • 📊 Developed comprehensive vascular mapping pipeline for MRA data<br>
                    • 🏆 Published 10+ research papers demonstrating effectiveness of graph models<br>
                    • 👥 Engaged with 50+ active researchers worldwide<br>
                    • 🌟 Successfully implemented ComBat harmonization method for dataset integration
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def about_page():
    """Main function to display the About Us page."""
    # Set page config
    st.set_page_config(
        page_title="About Us - BrainArteryNet",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom styling
    set_page_style()
    
    # Hide streamlit default elements
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # Add navigation bar
    st.markdown("""
        <div class="nav-container">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px;">
                <div class="logo-text">
                    🧠 BrainArteryNetwork
                </div>
                <div style="display: flex; gap: 20px;">
                    <a href="/Data_Visualization" class="nav-link">Datasets</a>
                    <a href="/PandasAI" class="nav-link">Analysis</a>
                    <a href="https://wxdrizzle.github.io/MOCHA_documents/Vessel%20Voyager/" target="_blank" class="nav-link">Software</a>
                    <a href="/About_Us" class="nav-link">About Us</a>
                    <a href="/Login" class="nav-link login-btn">Login/Sign-up</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Display page sections
    mission_section()
    team_section()
    achievements_section()

if __name__ == "__main__":
    about_page() 