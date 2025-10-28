import streamlit as st
from PIL import Image
import base64
import time

# Function to get base64 image (not strictly needed for local files but good practice)
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title="Happy Birthday, Raju!",
    page_icon="🎈",
    layout="centered", # Optimized for phone screens
    initial_sidebar_state="collapsed" # Hides sidebar on mobile
)

# Custom CSS for a festive and mobile-friendly look
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6; /* Light gray background */
        background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%239C92AC' fill-opacity='0.15' fill-rule='evenodd'%3E%3Cpath d='M0 0h30v30H0V0zm30 30h30v30H30V30z'/%3E%3C/g%3E%3C/svg%3E");
        text-align: center;
        padding: 10px; /* Reduced padding for mobile */
    }
    .stApp {
        text-align: center;
    }
    h1 {
        color: #ff6347; /* Tomato red for main heading */
        font-size: 2.5em; /* Smaller for mobile */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        margin-bottom: 0.5em;
    }
    h2 {
        color: #4682b4; /* Steel blue for subheadings */
        font-size: 1.5em; /* Smaller for mobile */
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }
    .birthday-message {
        font-size: 1.1em; /* Adjusted for mobile readability */
        color: #B6FCD5;
        margin-top: 15px;
        margin-bottom: 15px;
        line-height: 1.4;
    }
    .balloon-emoji {
        font-size: 2em; /* Smaller emoji for mobile */
        animation: float 4s ease-in-out infinite;
        display: inline-block;
        opacity: 0; /* Hidden initially */
        transition: opacity 1s ease-in; /* Fade-in effect */
    }
    .balloon-emoji.visible {
        opacity: 1; /* Visible after delay */
    }
    @keyframes float {
        0% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }
    .stImage > img { /* Target the actual image tag inside st.image */
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        max-width: 95%; /* Adjust image size for mobile */
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .stImage { /* Container for the image, for centering */
        display: flex;
        justify-content: center;
    }
    .stInfo {
        margin-top: 20px;
        margin-bottom: 20px;
        font-size: 0.9em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- App Content ---

st.title(f"🎉 Happy Birthday, Raju! 🎉")

st.markdown("<div class='birthday-message'>My dearest friend Raju, on your special day, I wish you nothing but boundless joy, incredible adventures, and all the success you truly deserve! May this new year of your life be the best one yet.</div>", unsafe_allow_html=True)

# Display Raju's photo
try:
    raju_image = Image.open('image.png') # Ensure this path is correct
    # Rectified: using use_container_width instead of use_column_width
    st.image(raju_image, caption="To my incredible friend, Raju!", use_container_width=True)
except FileNotFoundError:
    st.error("Oops! Raju's birthday image isn't here.")
    st.markdown("Please make sure the image `raju_birthday.png` is in the same folder as this script.")
    st.markdown("If you've named it differently or saved it as a `.jpg`, please adjust the `Image.open('raju_birthday.png')` line in the code accordingly.")
except Exception as e:
    st.error(f"An unexpected error occurred while loading the image: {e}")
    st.markdown("Please double-check the image file for corruption or incorrect format.")


st.markdown("---")

st.markdown("<h2>Here's to a year filled with laughter, new memories, and achieving all your dreams!</h2>", unsafe_allow_html=True)
st.markdown("<div class='birthday-message'>From conquering new challenges to celebrating small victories, may every moment bring you closer to happiness. You're an amazing friend, and I'm so grateful for you!</div>", unsafe_allow_html=True)


# Delayed balloon effect
# Use st.empty to create a placeholder that can be updated
balloon_placeholder = st.empty()

# Add a slight delay before showing balloons
# This simulates the "after 1 sec of loading" for the interactive elements.
time.sleep(1)

with balloon_placeholder:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("<div class='balloon-emoji visible'>🎈</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='balloon-emoji visible'>🎁</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='balloon-emoji visible'>🎉</div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='balloon-emoji visible'>🎂</div>", unsafe_allow_html=True)
    with col5:
        st.markdown("<div class='balloon-emoji visible'>🥳</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.info("A little website made just for you by your close friend – because you deserve all the best!")

st.markdown("<br><br>", unsafe_allow_html=True)
st.write("---")

st.write("Crafted with ❤️ for Raju on his special day.")

