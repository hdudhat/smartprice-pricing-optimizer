# 💡 SmartPrice: AI-Powered Menu Pricing Optimizer

SmartPrice is an intelligent pricing optimization tool designed for restaurants and hospitality businesses. It uses machine learning to simulate how price affects demand and recommends the **optimal price per menu item** to maximize profit — all wrapped in a simple Streamlit web app.

---

## 🧠 Problem Statement

Most restaurants set menu prices based on intuition, competitor benchmarking, or fixed markups. This often leads to:

- Underpricing: Missing out on revenue
- Overpricing: Losing customers
- No dynamic pricing model
- No data-driven strategy

---

## 🚀 Solution

SmartPrice solves this by using **machine learning** to:
- Predict how many items will sell at different prices
- Simulate profit across price ranges
- Find the **sweet spot** — the price that gives the **maximum profit**
- Show the result in a visual + downloadable format via Streamlit

---

## 📊 Features

✅ Upload your menu dataset (CSV)  
✅ Predict demand using trained Random Forest model  
✅ Simulate pricing from £5 to £30  
✅ Find optimal price for every item  
✅ Download the optimized price list  
✅ Built with Python, scikit-learn, Streamlit

---

## 📁 Sample Data Format

| Item     | Category | Price | Cost_per_Item | Customer_Rating | Daily_Sales |
|----------|----------|-------|----------------|------------------|--------------|
| Pasta    | Main     | 14.99 | 6.50           | 4.5              | 40           |
| Lemonade | Drink    | 3.99  | 1.20           | 4.8              | 55           |

You can simulate data or use your own menu with these columns.

---

## 🧪 Tech Stack

- Python 🐍
- pandas, numpy, scikit-learn
- Streamlit 🌐
- Matplotlib (for local profit curve)
- Joblib (to save model)

---

## 📷 Screenshots

> Include a screenshot of:
- App UI with file upload
- Optimized pricing table
- Sample profit vs. price curve

---

## 🛠️ How to Run Locally

1. Clone the repo or download the files  
2. Install dependencies:

```bash
pip install -r requirements.txt
