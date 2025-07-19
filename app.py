import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("smartprice_sales_model.pkl")

# Title
st.title("💡 SmartPrice: Menu Pricing Optimizer")
st.markdown("Upload your restaurant menu data to calculate the **optimal price per item** to maximize **profit**.")

# Upload CSV
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

# Optimization function
def find_optimal_profit_price(row, model, category_cols):
    prices = np.linspace(5, 30, 50)
    profits = []

    for price in prices:
        features = [price, row['Customer_Rating']]
        for col in category_cols:
            features.append(row.get(col, 0))

        predicted_sales = model.predict([features])[0]
        profit = (price - row['Cost_per_Item']) * predicted_sales
        profits.append(profit)

    best_index = np.argmax(profits)
    return prices[best_index], profits[best_index]

# On file upload
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # One-hot encode categories
    df = pd.get_dummies(df, columns=['Category'], drop_first=True)

    # Get category columns used during model training
    category_cols = [col for col in df.columns if 'Category_' in col]

    # Calculate optimal prices
    df['Optimal_Price'] = df.apply(lambda row: find_optimal_profit_price(row, model, category_cols)[0], axis=1)
    df['Expected_Profit'] = df.apply(lambda row: find_optimal_profit_price(row, model, category_cols)[1], axis=1)

    # Display table
    st.subheader("🔍 Optimized Pricing Recommendations")
    st.dataframe(df[['Item', 'Price', 'Optimal_Price', 'Expected_Profit', 'Customer_Rating']])

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Optimized CSV", data=csv, file_name="smartprice_optimized_output.csv", mime="text/csv")
