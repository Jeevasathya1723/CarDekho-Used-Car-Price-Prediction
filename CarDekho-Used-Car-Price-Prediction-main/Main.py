import streamlit as st
from streamlit_option_menu import option_menu
import Home, Filtering, Analysis, Prediction
from PIL import Image

# Define the correct image path
image_path = r"C:\Users\Aruji\OneDrive\Desktop\Jeeva\CarDekho-Used-Car-Price-Prediction-main\image.jpg"

# Try to load the image
try:
    img = Image.open(image_path)
except FileNotFoundError:
    st.warning(f"⚠️ Image file not found at {image_path}. Please verify the file path.")
    img = None  # Fallback if the image is missing

# Set Streamlit Page Config (must be the first Streamlit command)
st.set_page_config(
    page_title="CarDekho Resale Price Prediction",
    page_icon=img if img else None,
    layout="wide"
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({'title': title, 'function': function})

    def run(self):
        with st.sidebar:
            app = option_menu(
                "Car Resale Price Prediction",
                ["Home", "Data Filtering", "Data Analysis", "Data Prediction"],
                icons=['house', 'search', "reception-4", "dice-5-fill"],
                menu_icon="cash-coin",
                default_index=0,
                orientation="vertical",
                styles={
                    "container": {"padding": "0!important", "background-color": "#A95C68"},
                    "icon": {"color": "violet", "font-size": "20px"},
                    "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#C4A484"},
                    "nav-link-selected": {"background-color": "#C04000"},
                }
            )

        # Navigate between pages
        if app == "Home":
            Home.app()
        elif app == "Data Filtering":
            Filtering.app()
        elif app == "Data Analysis":
            Analysis.app()
        elif app == "Data Prediction":
            Prediction.app()

# Initialize and run the multi-page app
app = MultiApp()
app.add_app("Home", Home.app)
app.add_app("Data Filtering", Filtering.app)
app.add_app("Data Analysis", Analysis.app)
app.add_app("Data Prediction", Prediction.app)
app.run()
