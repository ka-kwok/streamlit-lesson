import streamlit as st  # Import Streamlit for web app functionality
from app_pages.multi_page import MultiPage  # Import MultiPage class for multi-page app structure
from app_pages.page_calculator import calculator_body  # Import the calculator page content

app = MultiPage(app_name="Calculator App")  # Create a MultiPage app instance with a name

app.add_page("Calculator", calculator_body)  # Add the calculator page to the app

app.run()  # Run the Streamlit app
