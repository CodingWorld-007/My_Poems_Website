import streamlit as st
from PIL import Image

# Function to load images
def load_image(image_path):
    return Image.open(image_path)

# Function to load and inject CSS
def load_css(css_file_path):
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load external CSS file
load_css("styles.css")

# Add a sidebar with poem options
st.sidebar.header("Choose a Poem")

# Define poem options
poem_options = {
    "The Happy hours of Life": "Poems/Poem1.jpg",
    "Just Go with the flow": "Poems/Poem4.jpg",
    "Nobody is here": "Poems/Poem3.jpg",
    "I Don't know why ? ": "Poems/Poem5.jpg",
    "Its the End of Journey": "Poems/Poem2.jpg",
    "Reality is Money": "Poems/Poem6.jpg"
}

# Create a select box in the sidebar for poem selection
selected_poem = st.sidebar.selectbox("Click below:", list(poem_options.keys()))

# Set the title of the app dynamically based on the selected poem
st.title(f"POEM - {selected_poem}")

# Load and display the selected poem image
if selected_poem:
    image_path = poem_options[selected_poem]
    st.sidebar.markdown("---")
    image = load_image(image_path)
    st.image(image, caption=selected_poem, use_column_width=True)
    if st.sidebar.button("About Author"):
        st.sidebar.markdown("[LinkedIn](www.linkedin.com/in/amanajjoshi)")
# Add button for "About Author"
