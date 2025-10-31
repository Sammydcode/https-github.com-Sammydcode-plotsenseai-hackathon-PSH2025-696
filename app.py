import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotsense as ps
import joblib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set PlotSense API
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found! Please set it in your environment or .env file.")

explainer = ps.PlotExplainer()

# Load dataset
df = pd.read_csv(r"preprocessed_data.csv")

# Title
st.title("Credit Card Transaction Anomaly Detector")

# User input
st.header("Enter Transaction Details")
amount = st.number_input("Transaction Amount")
transaction_speed = st.number_input("Transaction Speed")

# Create transaction DataFrame
transaction = pd.DataFrame({
    'Amount': [amount],
    'transaction_speed': [transaction_speed],
    'account_balance': [5000],
    'transaction_frequency': [3],
    'customer_age': [35],
    'card_usage_pattern': [1],
    'merchant_reputation': [0.8],
    'card_limit_ratio': [0.3],
    'geo_distance': [5],
    'time_of_day': [14],
    'customer_income_level': [4000],
    'account_activity_score': [0.5],
    'ip_address_risk': [0.1],
    'region_risk_factor': [0.2],
    'customer_behavior_score': [0.6],
    'login_pattern': [0.8],
    'security_score': [0.7],
    'transaction_device_history': [0.2],
    'merchant_device_trust_score': [0.9],
})

# Hybrid Scoring
from module.hybrid_analyzer import HybridAnomalyAnalyzer

features = [
    'account_balance','transaction_speed','transaction_frequency','customer_age',
    'card_usage_pattern','merchant_reputation','card_limit_ratio','geo_distance',
    'time_of_day','customer_income_level','account_activity_score','ip_address_risk',
    'region_risk_factor','customer_behavior_score','login_pattern','security_score',
    'transaction_device_history','merchant_device_trust_score','Amount'
]

# Initialize and compute hybrid score
analyzer = HybridAnomalyAnalyzer(
    model_path="isolation_forest_model.pkl",
    api_key=os.getenv("GROQ_API_KEY")  # reusinf the API key from env
)
results = analyzer.hybrid_score(transaction, features)
rule_score = results['rule_score']
anomaly_score = results['anomaly_score']
final_score = results['final_score']
flag = results['flag']


# Display scores
st.subheader("Prediction Scores")
st.write(f"Rule Score: {rule_score:.2f}")
st.write(f"Anomaly Score: {anomaly_score:.2f}")
st.write(f"Final Score: {final_score:.2f}")
st.write(f"Suspicious Transaction: {'Yes!' if flag else 'No'}")

# Visualization
st.subheader("Visualizations")

if flag:
    flagged_df = transaction
else:
    flagged_df = pd.DataFrame()

if not flagged_df.empty:
    # Basic scatter plot
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(flagged_df['Amount'], flagged_df['transaction_speed'], color='red', label='Flagged')
    ax.scatter(transaction['Amount'], transaction['transaction_speed'], color='blue', marker='x', s=100, label='Current Transaction')
    ax.set_xlabel("Amount")
    ax.set_ylabel("Transaction Speed")
    ax.set_title("Suspicious Transactions")
    ax.legend()
    st.pyplot(fig)

    

    # Create a safe temporary directory for storing plots
    TEMP_DIR = os.path.join(os.getcwd(), "temp_files")
    os.makedirs(TEMP_DIR, exist_ok=True)

    # Define a global temp plot path
    TEMP_PLOT_PATH = os.path.join(TEMP_DIR, "temp_plot.jpg")


    # PlotSense Explanation
    chart_info = {"chart_type": "scatter", "columns": ["Amount", "transaction_speed"]}
    fig.savefig("temp_plot.jpg")  # Save the figure first
    insight = explainer.refine_plot_explanation(fig, chart_info)
    st.subheader("PlotSense Insights")
    st.write(insight)

    # Advanced Analytical Module
    st.subheader("Flagged Transactions Statistics")
    stats = flagged_df[['Amount', 'transaction_speed']].agg(['mean','median','min','max'])
    st.write(stats)

    st.subheader("Current Transaction vs Stats")
    comparison = {
        'Amount_vs_mean': transaction['Amount'].iloc[0] - stats.loc['mean','Amount'],
        'Speed_vs_mean': transaction['transaction_speed'].iloc[0] - stats.loc['mean','transaction_speed']
    }
    st.write(comparison)

else:
    st.write("No flagged transactions to display or explain.")
