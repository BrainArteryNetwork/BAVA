"""
    This module displays the home page of the Brain Artery Visualization and Analysis app.
    This is the landing page. Pages are organized as per multi-page streamlit app design.
    All new pages will go in streamlit/pages/ dir.
    Title of the page is the filename.
"""
import streamlit as st
import os
from pathlib import Path

def get_asset_path(filename):
    """Get the full path for an asset file."""
    current_dir = Path(__file__).parent
    root_dir = current_dir.parent
    return os.path.join(root_dir, 'static', 'images', filename)

def set_custom_style():
    """Set custom CSS styles for the page."""
    st.markdown("""
        <style>
        /* Main background and text colors */
        .stApp {
            background: linear-gradient(to bottom, rgba(10, 25, 47, 0.95), rgba(23, 42, 70, 0.95));
            color: white;
            background-image: url('https://raw.githubusercontent.com/BrainArteryNetwork/BAVA/main/bava/static/images/banner_background.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
        }
        
        /* Navigation styling */
        .nav-container {
            padding: 20px 0;
            background: rgba(10, 25, 47, 0.8);
            backdrop-filter: blur(10px);
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }
        
        .nav-link {
            color: white !important;
            text-decoration: none;
            margin: 0 20px;
            font-size: 16px;
            font-weight: 500;
            transition: color 0.3s ease;
            padding: 8px 16px;
            border-radius: 20px;
        }
        
        .nav-link:hover {
            color: #ffa500 !important;
            background: rgba(255, 165, 0, 0.1);
        }
        
        /* Logo styling */
        .logo-text {
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            font-weight: bold;
            color: white;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .logo-text img {
            height: 40px;
            width: auto;
        }
        
        /* Button styling */
        .get-started-btn {
            background: linear-gradient(90deg, #ffa500, #ff8c00);
            color: white;
            padding: 15px 40px;
            border-radius: 30px;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
            border: none;
            margin-top: 20px;
        }
        
        .get-started-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 165, 0, 0.3);
        }
        
        /* Tagline styling */
        .tagline {
            font-size: 48px;
            font-weight: bold;
            line-height: 1.2;
            margin-top: 180px;
            margin-bottom: 40px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            opacity: 0;
            animation: fadeIn 1s ease-out forwards;
        }
        
        /* Wave decoration */
        .wave-bottom {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 150px;
            background: linear-gradient(to right, #ffa500, #ff8c00);
            clip-path: ellipse(60% 60% at 50% 100%);
            z-index: -1;
        }
        
        /* Animations */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Login button special styling */
        .login-btn {
            background: rgba(255, 165, 0, 0.2);
            border: 1px solid #ffa500;
            color: white !important;
            padding: 8px 20px;
            border-radius: 20px;
            transition: all 0.3s ease;
        }
        
        .login-btn:hover {
            background: rgba(255, 165, 0, 0.3);
            transform: translateY(-2px);
        }
        
        /* Stats section */
        .stats-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 40px;
            animation: fadeIn 1s ease-out 0.5s forwards;
        }
        
        .stat-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px 50px;
            border-radius: 15px;
            text-align: center;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 165, 0, 0.2);
            transition: transform 0.3s ease;
        }
        
        .stat-item:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 165, 0, 0.5);
        }
        
        .stat-number {
            font-size: 48px;
            font-weight: bold;
            color: #ffa500;
            margin-bottom: 10px;
        }
        
        .stat-label {
            font-size: 16px;
            color: rgba(255, 255, 255, 0.8);
        }
        
        /* Mission and Vision styling */
        .mission-vision-container {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        
        .mission-box {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            width: 45%;
            min-width: 300px;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 165, 0, 0.2);
            transition: transform 0.3s ease;
        }
        
        .mission-box:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 165, 0, 0.5);
        }
        
        .section-title {
            font-size: 28px;
            font-weight: bold;
            color: #ffa500;
            margin-bottom: 20px;
        }
        
        .section-content {
            font-size: 18px;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.9);
        }
        </style>
    """, unsafe_allow_html=True)

def navigation_bar():
    """Create the navigation bar."""
    st.markdown("""
        <div class="nav-container">
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])
    
    with col1:
        st.markdown("""
            <div class="logo-text">
                🧠 BrainArteryNetwork
                <div style="font-size: 14px; font-weight: normal;"></div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<a href="/Data_Visualization" class="nav-link">Datasets</a>', unsafe_allow_html=True)
    with col3:
        st.markdown('<a href="/PandasAI" class="nav-link">Analysis</a>', unsafe_allow_html=True)
    with col4:
        st.markdown('<a href="https://wxdrizzle.github.io/MOCHA_documents/Vessel%20Voyager/" target="_blank" class="nav-link">Software</a>', unsafe_allow_html=True)
    with col5:
        st.markdown('<a href="/About_Us" class="nav-link">About Us</a>', unsafe_allow_html=True)
    with col6:
        st.markdown('<a href="/Login" class="nav-link login-btn">Login/Sign-up</a>', unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)

def main_content():
    """Create the main content section."""
    # Main title and introduction
    st.markdown("""
        <div style="text-align: center; margin-top: 60px; margin-bottom: 60px;">
            <div style="font-size: 56px; font-weight: bold; margin-bottom: 20px; color: #ffa500;">
                BAVA
            </div>
            <div style="font-size: 24px; margin-bottom: 10px; color: white;">
                Brain Artery Visualization & Analysis Tool
            </div>
            <div style="font-size: 18px; line-height: 1.6; max-width: 800px; margin: 0 auto; color: rgba(255, 255, 255, 0.9);">
                BAVA is a cutting-edge online platform designed for medical researchers focusing on neurology, 
                particularly in the study of brain artery networks. It integrates powerful visualization tools 
                with statistical analysis and artificial intelligence (AI) capabilities to facilitate the 
                exploration and analysis of vascular diseases.
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Stats section
    st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">500+</div>
                <div class="stat-label">Brain Scans Analyzed</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">10+</div>
                <div class="stat-label">Research Papers</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">50+</div>
                <div class="stat-label">Active Researchers</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Mission and Vision
    st.markdown("""
        <div style="text-align: center; margin-top: 60px;">
            <div class="mission-vision-container">
                <div class="mission-box">
                    <div class="section-title">Our Mission</div>
                    <div class="section-content">
                        To establish a standardized framework for analyzing brain artery networks, advancing our 
                        understanding of neurovascular health across diverse populations.
                    </div>
                </div>
                <div class="mission-box">
                    <div class="section-title">Our Vision</div>
                    <div class="section-content">
                        To revolutionize early diagnosis and treatment of neurovascular conditions through 
                        advanced brain artery network analysis and visualization.
                    </div>
                </div>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 40px;">
            <a href="/Data_Visualization" class="get-started-btn">⚡ Start Exploring</a>
        </div>
    """, unsafe_allow_html=True)

def wave_decoration():
    """Add the wave decoration at the bottom."""
    st.markdown("""
        <div class="wave-bottom"></div>
    """, unsafe_allow_html=True)

def home_page():
    # Set page config
    st.set_page_config(
        page_title="BrainArteryNetwork",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Apply custom styling
    set_custom_style()
    
    # Hide streamlit default elements
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    # Build the page
    navigation_bar()
    main_content()
    wave_decoration()

if __name__ == "__main__":
    home_page()