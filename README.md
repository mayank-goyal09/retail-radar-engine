# RETAIL RADAR ENGINE

ML-powered customer segmentation system using RFM analysis and K-Means clustering to identify high-value customers from retail transactions | Streamlit Web App

## Overview

Retail Radar Engine is an intelligent customer segmentation system that uses RFM Analysis (Recency, Frequency, Monetary) combined with K-Means Clustering to identify and categorize high-value customers from retail transaction data.

This project demonstrates how machine learning can be leveraged to optimize marketing strategies, improve customer retention, and maximize business revenue through data-driven customer insights.

## Key Features

✓ RFM Analysis - Calculate Recency, Frequency, and Monetary values for each customer
✓ Smart Clustering - K-Means algorithm to segment customers into distinct groups
✓ Interactive Dashboard - Real-time visualization using Streamlit
✓ Pre-trained Models - Ready-to-use joblib models for instant predictions
✓ Sample Data - Dummy retail dataset for testing and demonstration
✓ Production Ready - Scalable architecture for real-world applications

## Project Structure

retail-radar-engine/
├── app.py (21.5 KB) - Main Streamlit web application
├── main.ipynb (170 KB) - EDA & Model Training Notebook
├── requirements.txt - Python dependencies
├── README.md - Project documentation
├── Models/
│  ├── rfm_kmeans_k2.joblib - Trained K-Means model (K=2 clusters)
│  └── rfm_scaler.joblib - StandardScaler for feature normalization
└── Data/
   ├── rfm_segments.csv - Pre-computed customer segments (206 KB)
   ├── dummy_retail.csv - Sample transaction data
   └── make_dummy_csv.py - Script to generate demo data

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. Clone the Repository
```bash
git clone https://github.com/mayank-goyal09/retail-radar-engine.git
cd retail-radar-engine
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

### Running Locally

```bash
streamlit run app.py
```

The app will open in your browser at http://localhost:8501

## How It Works

### RFM Analysis

RFM is a customer segmentation technique based on three key metrics:

1. **Recency (R)**: Days since last purchase
   - Lower values indicate more recent customers
   
2. **Frequency (F)**: Total number of purchases
   - Higher values indicate loyal customers
   
3. **Monetary (M)**: Total spending amount
   - Higher values indicate high-value customers

### K-Means Clustering

After calculating RFM values:
1. Features are normalized using StandardScaler
2. K-Means algorithm groups customers into distinct segments
3. Each segment represents a customer cohort with similar behavior patterns

## Dataset Features

| Column | Description |
|--------|-------------|
| customer_id | Unique customer identifier |
| transaction_date | Date of purchase |
| purchase_amount | Amount spent in transaction |
| product_category | Product category purchased |
| quantity | Number of items purchased |

## Usage

### Via Streamlit Web App

1. Visit [Retail Radar Engine](https://retail-radar-engine-project.streamlit.app/)
2. Upload your retail transaction CSV file
3. View customer segments and analytics
4. Download segmented customer list

### Via Python Code

```python
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load pre-trained models
scaler = joblib.load('rfm_scaler.joblib')
kmeans = joblib.load('rfm_kmeans_k2.joblib')

# Prepare RFM data
rfm_data = pd.read_csv('rfm_segments.csv')
X = rfm_data[['Recency', 'Frequency', 'Monetary']]

# Scale features
X_scaled = scaler.transform(X)

# Predict segments
segments = kmeans.predict(X_scaled)
rfm_data['Segment'] = segments

print(rfm_data.head())
```

## Technologies Used

- streamlit >= 1.28.0 - Interactive web framework
- pandas >= 1.5.0 - Data manipulation
- numpy >= 1.24.0 - Numerical computing
- scikit-learn >= 1.3.0 - Machine learning algorithms
- joblib >= 1.3.0 - Model serialization
- plotly >= 5.17.0 - Interactive visualizations
- python-dateutil >= 2.8.2 - Date utilities

## Learning Outcomes

This project demonstrates:

✓ Data Analysis - EDA and customer data exploration
✓ Feature Engineering - Computing RFM metrics from raw transactions
✓ Machine Learning - Implementing K-Means clustering algorithm
✓ Model Persistence - Serializing models with joblib
✓ Web Development - Building interactive Streamlit dashboards
✓ Data Visualization - Creating meaningful business insights
✓ GitHub - Version control and repository management

## Business Applications

- **Targeted Marketing** - Design campaigns for specific customer segments
- **Customer Retention** - Identify at-risk customers for intervention
- **Revenue Optimization** - Focus resources on high-value customers
- **Inventory Management** - Stock products based on segment preferences
- **Personalization** - Customize offers based on segment behavior

## Notebook Analysis

**main.ipynb** includes:

1. **Data Loading & Cleaning** - Process raw transaction data
2. **Exploratory Data Analysis (EDA)** - Visualize customer patterns
3. **RFM Calculation** - Compute metrics for each customer
4. **Feature Scaling** - Normalize features for clustering
5. **Model Training** - Train K-Means with optimal K value
6. **Evaluation** - Analyze cluster characteristics
7. **Model Export** - Save trained models as joblib files

## Results & Insights

Segmented customers are saved in `rfm_segments.csv` with:
- Customer ID & RFM metrics
- Assigned cluster/segment
- Segment characteristics and recommendations

## Future Enhancements

- [ ] Add more clustering algorithms (Hierarchical, DBSCAN)
- [ ] Implement time-series customer behavior analysis
- [ ] Add predictive churn modeling
- [ ] Create customer lifetime value (CLV) predictions
- [ ] Develop advanced data visualization dashboard
- [ ] Add machine learning model explainability (SHAP)
- [ ] Implement real-time data pipeline
- [ ] Add A/B testing framework for campaigns

## Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## About Author

**Mayank Goyal** | Data Science Enthusiast

- GitHub: [@mayank-goyal09](https://github.com/mayank-goyal09)
- Portfolio: Building ML projects for real-world impact
- Focus: Customer analytics, ML systems, Data engineering

## Support

If you found this project helpful:

- Star the repository
- Watch for updates
- Share with your network
- Open an issue for suggestions

## Useful Links

- [Live Streamlit App](https://retail-radar-engine-project.streamlit.app/)
- [GitHub Repository](https://github.com/mayank-goyal09/retail-radar-engine)
- [RFM Analysis Guide](https://en.wikipedia.org/wiki/RFM_(customer_value))
- [K-Means Clustering](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**Made with ❤️ by Mayank Goyal** | Last Updated: December 2025
