
# Customer Segmentation Project

## Overview
This project implements a Customer Segmentation system using unsupervised learning (KMeans clustering) in Python. The goal is to segment customers into different groups based on their age, annual income, and spending score to enable targeted marketing strategies and better customer understanding.

---

## Features
- Data preprocessing with scaling using `StandardScaler`
- Customer segmentation using KMeans clustering
- REST API for prediction built with FastAPI
- Interactive dashboard using Streamlit for user input and visualization
- PCA-based cluster visualization
- Dockerized deployment for both API and dashboard
- Logging and error handling for robust production-level usage
- Unit tests for key components

---

## Project Structure
```
customer_segmentation/
│
├── api/
│   └── main.py                 # FastAPI application for serving predictions
│
├── src/
│   ├── data_processing.py      # Data loading and preprocessing
│   ├── feature_engineering.py  # Scaler save/load and feature engineering
│   ├── model.py                # Model training, saving, loading, prediction
│   └── utils.py                # Utility functions including logging config
│
├── streamlit_app/
│   └── dashboard.py            # Streamlit UI for interactive prediction and visualization
│
├── data/
│   └── raw/
│       └── customers.csv       # Sample customer data (age, income, spending score)
│
├── tests/
│   ├── test_model.py           # Unit tests for model module
│   └── test_feature_engineering.py # Unit tests for scaler and features
│
├── Dockerfile.api              # Dockerfile for FastAPI backend
├── Dockerfile.dashboard        # Dockerfile for Streamlit dashboard
├── docker-compose.yml          # Compose file to run API and dashboard together
├── requirements.txt            # Python dependencies
├── run_pipeline.py             # Script to preprocess data, train model and save artifacts
├── README.md                   # Project documentation
└── .gitignore
```

---

## How It Works

1. **Data Preparation:** The pipeline loads customer data from CSV, selects relevant features (Age, Annual Income, Spending Score), and scales them.
2. **Model Training:** A KMeans clustering model is trained on scaled features to segment customers into clusters (default 4 clusters).
3. **API:** FastAPI serves prediction requests where users submit customer info and get back the predicted segment.
4. **Dashboard:** Streamlit app allows users to interactively input customer details, get segment prediction, and visualize cluster distribution using PCA.
5. **Deployment:** Docker containers run the API and dashboard for easy deployment and scalability.

---

## Usage

### 1. Setup environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Train the model and generate artifacts
```bash
python run_pipeline.py
```

### 3. Run FastAPI backend
```bash
uvicorn api.main:app --reload
```
Visit `http://127.0.0.1:8000/docs` to access API docs.

### 4. Run Streamlit dashboard
```bash
streamlit run streamlit_app/dashboard.py
```
Visit `http://localhost:8501` in your browser.

### 5. Docker (optional)
Build and run all services:
```bash
docker compose up --build
```

---

## Model Details

- **Algorithm:** KMeans Clustering
- **Features:** Age, Annual Income (k$), Spending Score (1-100)
- **Clusters:** 4 (default)
- **Purpose:** Group customers based on purchasing behavior and demographics for targeted marketing.

---

## Segment Descriptions (Example)

| Segment | Description                         |
|---------|-----------------------------------|
| 0       | Low income, low spending score     |
| 1       | High income, high spending score   |
| 2       | Young, moderate income, moderate spending |
| 3       | Middle-aged, high income, low spending |

*(Descriptions may vary based on data and model output)*

---

## Testing

Run tests with:
```bash
pytest tests/
```

---

## Logging & Error Handling

- Centralized logging configured in `src/utils.py`
- API and dashboard handle exceptions gracefully and show meaningful error messages

---

## Contribution

Feel free to fork, raise issues or contribute improvements.

---
