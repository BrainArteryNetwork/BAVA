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
            background-image: url('https://github.com/BrainArteryNetwork/BAVA/tree/main/bava/static/images/banner_background.png');
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
            padding: 12px 30px;
            border-radius: 25px;
            border: none;
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .get-started-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 165, 0, 0.3);
        }
        
        .get-started-btn::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                45deg,
                transparent,
                rgba(255, 255, 255, 0.1),
                transparent
            );
            transform: rotate(45deg);
            transition: all 0.3s ease;
        }
        
        .get-started-btn:hover::after {
            transform: rotate(45deg) translate(50%, 50%);
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
            margin-top: 60px;
            animation: fadeIn 1s ease-out 0.5s forwards;
            opacity: 0;
        }
        
        .stat-item {
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            backdrop-filter: blur(5px);
        }
        
        .stat-number {
            font-size: 36px;
            font-weight: bold;
            color: #ffa500;
        }
        
        .stat-label {
            font-size: 14px;
            color: rgba(255, 255, 255, 0.8);
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
                🧠 BrainArteryNet
                <div style="font-size: 14px; font-weight: normal;">Connect. Discover. Lead.</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<a href="/Leaderboard" class="nav-link">Leaderboard</a>', unsafe_allow_html=True)
    with col3:
        st.markdown('<a href="/Datasets" class="nav-link">Datasets</a>', unsafe_allow_html=True)
    with col4:
        st.markdown('<a href="/Analysis" class="nav-link">Analysis</a>', unsafe_allow_html=True)
    with col5:
        st.markdown('<a href="/About_Us" class="nav-link">About Us</a>', unsafe_allow_html=True)
    with col6:
        st.markdown('<a href="/Login" class="nav-link login-btn">Login/Sign-up</a>', unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)

def main_content():
    """Create the main content section."""
    # Main tagline with animation
    st.markdown("""
        <div class="tagline">
            "Decoding brain pathways<br>
            unlocks the keys to deeper discoveries<br>
            for a brighter tomorrow."
        </div>
    """, unsafe_allow_html=True)
    
    # Get Started button
    st.markdown("""
        <a href="/Analysis" class="get-started-btn">⚡ Get Started</a>
    """, unsafe_allow_html=True)
    
    # Stats section
    st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">1,000+</div>
                <div class="stat-label">Brain Scans Analyzed</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">50+</div>
                <div class="stat-label">Research Papers</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">100+</div>
                <div class="stat-label">Active Researchers</div>
            </div>
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
        page_title="BrainArteryNet - Connect. Discover. Lead.",
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