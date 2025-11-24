# 🎯 Customer Segmentation Project

## 📋 Overview
This project implements a Customer Segmentation system using unsupervised learning (KMeans clustering) in Python. The goal is to segment customers into different groups based on their age, annual income, and spending score to enable targeted marketing strategies and better customer understanding.

## ✨ Features
- 🔄 Data preprocessing with scaling using `StandardScaler`
- 🎯 Customer segmentation using KMeans clustering
- 🌐 REST API for prediction built with FastAPI
- 📊 Interactive dashboard using Streamlit for user input and visualization   
- 📈 PCA-based cluster visualization
- 🐳 Dockerized deployment for both API and dashboard
- 📝 Logging and error handling for robust production-level usage
- ✅ Unit tests for key components   

## 📁 Project Structure 
```
customer_segmentation/
├── 📂 data/                                # Contains raw and processed datasets
│   └── 📂 raw/
│       └── 📄 customers.csv                # Input CSV file with customer attributes
│
├── 📂 src/                                 # Core logic of the pipeline
│   ├── 📄 __init__.py                     # Package initialization
│   ├── 📄 config.py                       # Configuration settings
│   ├── 📄 data_loader.py                  # Data loading utilities
│   ├── 📄 preprocessing.py                # Data preprocessing functions
│   ├── 📄 feature_engineering.py          # Feature creation and scaling
│   ├── 📄 model.py                        # KMeans model implementation
│   ├── 📄 evaluate.py                     # Model evaluation metrics
│   ├── 📄 utils.py                        # Common utilities
│   └── 📄 logger.py                       # Logging configuration
│
├── 📂 api/                                 # FastAPI backend
│   └── 📄 main.py                         # FastAPI application
│
├── 📂 streamlit_app/                      # Streamlit frontend
│   └── 📄 dashboard.py                    # Interactive dashboard
│
├── 📂 models/                             # Model artifacts
│   ├── 📄 kmeans_model.pkl               # Trained KMeans model
│   └── 📄 scaler.pkl                     # Feature scaler
│
├── 📂 notebooks/                          # Jupyter notebooks
│   └── 📄 analysis.ipynb                 # Data analysis and visualization
│
├── 📂 tests/                              # Unit tests
│   ├── 📄 test_model.py                  # Model tests
│   └── 📄 test_feature_engineering.py    # Feature engineering tests
│
├── 📄 Dockerfile                          # Docker configuration
├── 📄 docker-compose.yml                 # Docker services orchestration
├── 📄 requirements.txt                    # Python dependencies
├── 📄 setup.py                           # Package setup
├── 📄 run_pipeline.py                    # Pipeline execution script
└── 📄 README.md                          # Project documentation
```

## 🚀 How It Works

1. **📊 Data Preparation:** 
   - Load customer data from CSV
   - Select features (Age, Annual Income, Spending Score)
   - Scale features using StandardScaler

2. **🤖 Model Training:** 
   - Train KMeans clustering model
   - Segment customers into 4 clusters
   - Save model and scaler artifacts

3. **🌐 API:** 
   - FastAPI backend for predictions
   - RESTful endpoints for customer segmentation
   - Input validation and error handling

4. **📊 Dashboard:** 
   - Interactive Streamlit interface
   - Real-time predictions
   - Cluster visualization with PCA
   - Customer segment insights

5. **🐳 Deployment:** 
   - Docker containers for API and dashboard
   - Easy deployment and scaling
   - Environment consistency

## 💻 Usage

### 1. Setup environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Train the model
```bash
python run_pipeline.py
```

### 3. Run FastAPI backend
```bash
uvicorn api.main:app --reload
```
Visit `http://127.0.0.1:8000/docs` for API documentation

### 4. Run Streamlit dashboard
```bash
streamlit run streamlit_app/dashboard.py
```
Visit `http://localhost:8501` in your browser

### 5. Docker deployment
```bash
docker compose up --build
```

## 📊 Model Details

- **Algorithm:** KMeans Clustering
- **Features:** 
  - Age
  - Annual Income (k$)
  - Spending Score (1-100)
- **Clusters:** 4 (default)
- **Purpose:** Customer grouping for targeted marketing

## 🎯 Segment Descriptions

| Segment | Description                         |
|---------|-----------------------------------|
| 0       | Low income, low spending score     |
| 1       | High income, high spending score   |
| 2       | Young, moderate income, moderate spending |
| 3       | Middle-aged, high income, low spending |

## 🧪 Testing

Run tests with:
```bash
pytest tests/
```

## 📝 Logging & Error Handling

- Centralized logging in `src/logger.py`
- Comprehensive error handling
- Meaningful error messages
- Production-ready logging configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- HARIHARANS24 - Initial work

## 🙏 Acknowledgments

- Thanks to all contributors
- Inspired by real-world customer segmentation needs







