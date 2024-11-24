
import streamlit as st
import pandas as pd

# Mock Data for the Prototype
mock_data = [
    {"Product Name": "Apple AirPods Pro (2nd Gen)", "Category": "Electronics", "Location": "Broward County",
     "Listing Price": 120, "Suggested Purchase Price": 100, "Estimated Resale Price": 180, "Profit Margin": 80,
     "Purchase Platform": "Facebook Marketplace", "Selling Platform": "eBay",
     "Ad Copy": "Apple AirPods Pro (2nd Gen) - Great condition! Fully functional. $180 OBO! Fast shipping available!",
     "Platform Justification": "High demand on eBay; better reach for electronics."},
    {"Product Name": "Dyson V8 Animal Vacuum", "Category": "Home Appliances", "Location": "Broward County",
     "Listing Price": 180, "Suggested Purchase Price": 160, "Estimated Resale Price": 300, "Profit Margin": 140,
     "Purchase Platform": "Craigslist", "Selling Platform": "OfferUp",
     "Ad Copy": "Dyson V8 Animal Vacuum - Like new, barely used! Perfect for pet owners. $300 OBO.",
     "Platform Justification": "OfferUp has strong local demand for home appliances."},
    {"Product Name": "Nintendo Switch Console", "Category": "Electronics", "Location": "Broward County",
     "Listing Price": 150, "Suggested Purchase Price": 130, "Estimated Resale Price": 220, "Profit Margin": 90,
     "Purchase Platform": "OfferUp", "Selling Platform": "Facebook Marketplace",
     "Ad Copy": "Nintendo Switch Console - Excellent condition! Includes dock and Joy-Cons. $220 OBO.",
     "Platform Justification": "Popular on Facebook Marketplace for quick flips."},
    {"Product Name": "Canon EOS Rebel T7 Camera", "Category": "Electronics", "Location": "Broward County",
     "Listing Price": 220, "Suggested Purchase Price": 200, "Estimated Resale Price": 400, "Profit Margin": 200,
     "Purchase Platform": "Facebook Marketplace", "Selling Platform": "OfferUp",
     "Ad Copy": "Canon EOS Rebel T7 - Great for photography enthusiasts! $400 OBO. Includes lens.",
     "Platform Justification": "Strong local demand for photography equipment."},
    {"Product Name": "Yamaha Acoustic Guitar", "Category": "Musical Instruments", "Location": "Broward County",
     "Listing Price": 90, "Suggested Purchase Price": 80, "Estimated Resale Price": 150, "Profit Margin": 70,
     "Purchase Platform": "OfferUp", "Selling Platform": "Facebook Marketplace",
     "Ad Copy": "Yamaha Acoustic Guitar - Great sound, excellent condition. $150 OBO.",
     "Platform Justification": "Local musicians favor Facebook Marketplace for instruments."}
]

# Convert data to a DataFrame
data_df = pd.DataFrame(mock_data)

# Streamlit App
st.title("FlipSmart: Turn Listings Into Earnings")
st.sidebar.header("Filter Options")

# Sidebar Filters
category = st.sidebar.selectbox("Select Category", ["All"] + list(data_df['Category'].unique()))
price_range = st.sidebar.slider("Price Range", 0, 300, (0, 300))

# Apply Filters
filtered_data = data_df[
    ((data_df['Category'] == category) | (category == "All")) &
    (data_df['Listing Price'] >= price_range[0]) & (data_df['Listing Price'] <= price_range[1])
]

# Display Results
st.subheader("Filtered Results")
if not filtered_data.empty:
    for index, row in filtered_data.iterrows():
        st.write(f"### {row['Product Name']}")
        st.write(f"**Category:** {row['Category']}")
        st.write(f"**Location:** {row['Location']}")
        st.write(f"**Listing Price:** ${row['Listing Price']}")
        st.write(f"**Suggested Purchase Price:** ${row['Suggested Purchase Price']}")
        st.write(f"**Estimated Resale Price:** ${row['Estimated Resale Price']}")
        st.write(f"**Profit Margin:** ${row['Profit Margin']}")
        st.write(f"**Purchase Platform:** {row['Purchase Platform']}")
        st.write(f"**Selling Platform:** {row['Selling Platform']}")
        st.write(f"**Ad Copy:** {row['Ad Copy']}")
        st.write(f"**Platform Justification:** {row['Platform Justification']}")
        st.write("---")
else:
    st.write("No results match your criteria.")

# Footer with branding
st.sidebar.write("**FlipSmart - Empowering Your Flipping Journey!**")
