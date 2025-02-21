import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Hugging Face API key (replace with your own token)
HUGGINGFACE_TOKEN = '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'

# URL for the Hugging Face Inference API
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"  # You can replace this with another model

# Function to call the Hugging Face Inference API
def query_huggingface_api(prompt):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_TOKEN}"
    }
    payload = {
        "inputs": prompt,
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()  # Raise an error if the response is not successful
    return response.content

# Streamlit UI
st.title('LogoCraft: Custom User Friendly logo Generator')

st.sidebar.header('Brand Description')
brand_name = st.sidebar.text_input('Brand Name', 'ExampleCorp')
brand_description = st.sidebar.text_area('Describe your brand', 'A tech company focused on innovation and creativity.')

# Generate logo based on description
if st.sidebar.button('Generate Logo'):
    with st.spinner("Generating logo..."):
        # Construct the prompt for the model
        prompt = f"Create a professional and memorable logo for a brand named {brand_name}. The logo should reflect the values and mission of the brand, which is: {brand_description}. The design should be modern, sleek, and unique."

        # Query the Hugging Face API to generate the logo
        try:
            image_bytes = query_huggingface_api(prompt)
            image = Image.open(BytesIO(image_bytes))
            st.image(image, caption='Generated Logo', use_column_width=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown('---')
st.markdown('LogoCraft uses cutting-edge AI to generate custom logos based on your brand description. Powered by Hugging Face and Streamlit.')
