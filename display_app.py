import streamlit as st
import pandas as pd

# Load CSV and force all columns to be read as strings
df = pd.read_csv("amazon_scraped_with_images.csv", dtype=str)

# Streamlit Page Setup
st.set_page_config(page_title="🛒 Amazon Scraped Products", layout="wide")
st.title("🛒 Amazon Scraped Products")

# Show total products
st.write(f"### Total Products: {len(df)}")

# Display Product Cards
for _, row in df.iterrows():
    with st.container():
        cols = st.columns([1, 3])

        with cols[0]:
            st.image(row["Image_URL"], width=150)

        with cols[1]:
            st.markdown(f"### [{row['Title']}]({row['Link']})")
            st.write(f"**Price:** {row['Price']}")
            st.write(f"**MRP:** {row['MRP']}")
            st.write(f"**Discount:** {row['Discount']}")
            st.markdown("---")
