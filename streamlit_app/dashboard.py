import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

from sklearn.decomposition import PCA

# Fix import path to include 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.model import load_model
from src.feature_engineering import load_scaler

# App title
st.title("🧠 Customer Segmentation Predictor")

# User input
age = st.slider("Age", 18, 70, 30)
income = st.slider("Annual Income (k$)", 10, 150, 50)
score = st.slider("Spending Score (1-100)", 1, 100, 50)

# Segment descriptions
segment_info = {
    0: {
        "label": "🧊 Cautious Spenders",
        "description": "Low income and low spending. Usually budget-conscious or inactive customers."
    },
    1: {
        "label": "💸 High Rollers",
        "description": "High income and high spending. These are your premium, loyal customers."
    },
    2: {
        "label": "📈 Potential Spenders",
        "description": "Young or moderate income, but spending heavily. Could be targeted for loyalty programs."
    },
    3: {
        "label": "🧮 Economical Customers",
        "description": "High income but low spending. May need product awareness or better targeting."
    }
}

# Predict button
if st.button("🔍 Predict Segment"):
    try:
        model = load_model()
        scaler = load_scaler()
        X = np.array([[age, income, score]])
        X_scaled = scaler.transform(X)
        segment = model.predict(X_scaled)[0]

        label = segment_info.get(segment, {}).get("label", f"Segment {segment}")
        desc = segment_info.get(segment, {}).get("description", "No description available.")

        st.success(f"🎯 Predicted Segment: {label}")
        st.info(f"💡 Insight: {desc}")

        # Download CSV
        pred_df = pd.DataFrame([[age, income, score, segment]], columns=["Age", "Income", "Score", "Segment"])
        csv = pred_df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇ Download Prediction CSV", csv, "prediction.csv", "text/csv")

    except Exception as e:
        st.error(f"Prediction failed: {e}")

# Divider
st.markdown("---")
st.subheader("📊 Cluster Visualization (PCA)")

# Optional visualization of clusters using PCA
if st.checkbox("Show Cluster Plot"):
    try:
        model = load_model()
        scaler = load_scaler()

        # Load customer data
        data = pd.read_csv("data/raw/customers.csv")
        X = data[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]
        X_scaled = scaler.transform(X)
        clusters = model.predict(X_scaled)

        # Reduce dimensions using PCA
        pca = PCA(n_components=2)
        components = pca.fit_transform(X_scaled)

        fig, ax = plt.subplots()
        scatter = ax.scatter(components[:, 0], components[:, 1], c=clusters, cmap="viridis", s=50)
        ax.set_title("Customer Segments (PCA Projection)")
        ax.set_xlabel("Component 1")
        ax.set_ylabel("Component 2")

        # Optional: Legend based on segment_info
        legend_labels = [segment_info.get(i, {}).get("label", f"Segment {i}") for i in np.unique(clusters)]
        handles = [plt.Line2D([0], [0], marker='o', color='w', label=legend_labels[i],
                              markerfacecolor=plt.cm.viridis(i / len(legend_labels)), markersize=8)
                   for i in range(len(legend_labels))]
        ax.legend(handles=handles, title="Segments", loc="best")

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Could not generate visualization: {e}")
