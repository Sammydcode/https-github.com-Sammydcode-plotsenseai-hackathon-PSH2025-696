import joblib
import numpy as np
import plotsense as ps
import os

class HybridAnomalyAnalyzer:
    def __init__(self, model_path, api_key):
        self.model = joblib.load(model_path)
        self.explainer = ps.PlotExplainer(api_keys={"groq": os.getenv("GROQ_API_KEY")})

    def hybrid_score(self, transaction, features):
        # --- Rule-based scoring ---
        rule_score = 0
        if transaction['Amount'].iloc[0] > 10000 and transaction['transaction_speed'].iloc[0] < 1:
            rule_score += 1
        rule_score = rule_score / 1

        # --- ML model scoring ---
        anomaly_score = 1 - self.model.decision_function(transaction[features].values.reshape(1, -1))[0]

        # --- Hybrid score ---
        alpha = 0.5
        final_score = alpha * rule_score + (1 - alpha) * anomaly_score
        flag = final_score > 0.5

        return {
            'rule_score': rule_score,
            'anomaly_score': anomaly_score,
            'final_score': final_score,
            'flag': flag
        }
