import streamlit as st
from PIL import Image
import base64
import io
from pathlib import Path

# Function to load images
def load_image(image_path):
    return Image.open(image_path)

# Function to convert image to base64
def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Function to load and inject CSS
def load_css(css_file_path):
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load external CSS file (assuming you have a 'styles.css' file in the same directory)
load_css("styles.css")

# Define poem options
poem_options = {
    "The Happy hours of Life": "Poems/Poem1.jpg",
    "Just Go with the flow": "Poems/Poem4.jpg",
    "Nobody is here": "Poems/Poem3.jpg",
    "I Don't know why ? ": "Poems/Poem5.jpg",
    "Its the End of Journey": "Poems/Poem2.jpg",
    "Reality is Money": "Poems/Poem6.jpg"
}

# Main content
selected_poem = st.sidebar.selectbox("Click below:", list(poem_options.keys()))

# Set the title of the app dynamically based on the selected poem
st.title(f"POEM - {selected_poem}")

# Load and display the selected poem image
if selected_poem:
    image_path = poem_options[selected_poem]
    image = load_image(image_path)
    st.markdown("---")
    # Download button to download poem image
    if st.button("Download Poem"):
        img_base64 = image_to_base64(image)
        href = f'data:image/jpeg;base64,{img_base64}'
        st.markdown(f'<a href="{href}" download="{selected_poem}.jpg">Click here to download the Image</a>', unsafe_allow_html=True)
    st.markdown("---")
    st.image(image, caption=selected_poem, use_column_width=True)
    st.markdown("---")
    st.sidebar.markdown("---")
    if st.sidebar.button("About Author"):
        st.sidebar.markdown("---")
        st.sidebar.markdown("[LinkedIn](www.linkedin.com/in/amanajjoshi)")
    
