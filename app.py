
import streamlit as st

st.set_page_config(page_title="Artisan Marketplace", layout="wide")

st.markdown("<h1 style='text-align: center; color: #8B4513;'>Handcrafted Traditions, Global Impact</h1>", unsafe_allow_html=True)
st.image("https://source.unsplash.com/1600x400/?artisan,crafts", use_column_width=True)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Shop", "Meet the Artisans", "Impact", "Contact"])

if page == "Home":
    st.markdown("## Explore Our Collections")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://source.unsplash.com/300x300/?handmade,jewelry", use_column_width=True)
        st.button("Shop Jewelry")
    with col2:
        st.image("https://source.unsplash.com/300x300/?handmade,textiles", use_column_width=True)
        st.button("Shop Textiles")
    with col3:
        st.image("https://source.unsplash.com/300x300/?handmade,ceramics", use_column_width=True)
        st.button("Shop Ceramics")

elif page == "Meet the Artisans":
    st.markdown("## Stories Behind the Craft")
    st.image("https://source.unsplash.com/1200x500/?artisan,craftspeople", use_column_width=True)

elif page == "Impact":
    st.markdown("## Our Impact")
    st.image("https://source.unsplash.com/1200x400/?sustainability,community", use_column_width=True)

elif page == "Contact":
    st.markdown("## Get in Touch")
    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.button("Send")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2025 Artisan Marketplace</p>", unsafe_allow_html=True)
