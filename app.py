import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Retail Radar Pro | Customer Segmentation",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# YELLOW + GREEN RETAIL THEME (IMPROVED TEXT VISIBILITY)
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Raleway', sans-serif;
}

/* Background: Fresh retail gradient (light yellow to green) */
.stApp {
    background: linear-gradient(135deg, #fefce8 0%, #fef9c3 25%, #ecfccb 60%, #d9f99d 100%);
    color: #1a1a1a;
}

.block-container {
    max-width: 1350px;
}

/* Hide default header */
[data-testid="stHeader"] {background: transparent;}
header {background: transparent;}

/* Hero Header */
.retail-hero {
    background: linear-gradient(135deg, #15803d 0%, #166534 60%);
    border-radius: 22px;
    padding: 20px 26px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 20px 50px rgba(21, 128, 61, 0.6);
    border: 3px solid #facc15;
    margin-bottom: 24px;
}
.hero-left {
    display: flex;
    gap: 18px;
    align-items: center;
}
.hero-icon {
    font-size: 3rem;
    padding: 14px;
    border-radius: 18px;
    background: radial-gradient(circle at 30% 20%, #fde047 0, #facc15 40%, #eab308 80%);
    box-shadow: 0 0 40px rgba(250, 204, 21, 0.9);
}
.hero-title {
    font-size: 2.1rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    color: #fef9c3;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.hero-sub {
    font-size: 0.95rem;
    color: #fef3c7;
    margin-top: 4px;
    font-weight: 500;
}
.hero-tag {
    display: inline-block;
    margin-top: 8px;
    font-size: 0.76rem;
    color: #1a1a1a;
    background: #fef9c3;
    border-radius: 999px;
    padding: 4px 12px;
    border: 1px solid #facc15;
    margin-right: 6px;
    font-weight: 700;
}
.hero-badge {
    font-size: 0.82rem;
    padding: 8px 16px;
    border-radius: 999px;
    background: #fef3c7;
    border: 2px solid #facc15;
    color: #1a1a1a;
    text-align: center;
    line-height: 1.4;
    font-weight: 800;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #fefce8 0%, #fef9c3 100%);
    border-right: 3px solid #22c55e;
}
[data-testid="stSidebar"] * {
    color: #1a1a1a !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #166534 !important;
    font-weight: 700;
}
.sidebar-section {
    font-size: 0.95rem;
    font-weight: 700;
    color: #166534 !important;
    margin-top: 1.3rem;
    margin-bottom: 0.4rem;
}

/* Main content text */
p, span, div {
    color: #1a1a1a;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.98);
    border-radius: 14px;
    border: 3px dashed #22c55e;
    padding: 1.2rem;
}
[data-testid="stFileUploader"] label {
    color: #166534 !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
}
[data-testid="stFileUploader"] section {
    color: #1a1a1a !important;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(120deg, #16a34a, #15803d);
    color: #ffffff !important;
    font-weight: 800;
    border-radius: 12px;
    border: none;
    padding: 0.7rem 1.6rem;
    font-size: 0.95rem;
    box-shadow: 0 8px 24px rgba(22, 163, 74, 0.5);
}
.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #14532d;
    color: #ffffff !important;
}

/* Download button special styling */
.stDownloadButton > button {
    background: linear-gradient(120deg, #facc15, #eab308) !important;
    color: #1a1a1a !important;
}
.stDownloadButton > button:hover {
    background: #ca8a04 !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 1rem 1.2rem;
    border: 3px solid #22c55e;
    box-shadow: 0 8px 24px rgba(34, 197, 94, 0.25);
}
[data-testid="stMetricLabel"] {
    color: #166534 !important;
    font-size: 0.82rem !important;
    text-transform: uppercase;
    font-weight: 700 !important;
}
[data-testid="stMetricValue"] {
    color: #15803d !important;
    font-weight: 800 !important;
    font-size: 1.6rem !important;
}
[data-testid="stMetricDelta"] {
    color: #166534 !important;
    font-weight: 600 !important;
}

/* Panel */
.retail-panel {
    background: #ffffff;
    border-radius: 18px;
    padding: 24px 26px;
    border: 3px solid #22c55e;
    box-shadow: 0 12px 32px rgba(34, 197, 94, 0.2);
    margin-bottom: 22px;
}
.panel-title {
    font-size: 1.2rem;
    font-weight: 800;
    color: #166534;
    margin-bottom: 8px;
}
.panel-sub {
    font-size: 0.88rem;
    color: #15803d;
    margin-bottom: 16px;
    font-weight: 500;
}

/* DataFrames */
[data-testid="stDataFrame"] {
    border-radius: 12px;
    border: 2px solid #22c55e;
}

/* Expander */
.streamlit-expanderHeader {
    background: #fef9c3;
    border-radius: 12px;
    border: 2px solid #22c55e;
    color: #166534 !important;
    font-weight: 700 !important;
}

/* Success/Info boxes */
.stSuccess {
    background: #dcfce7;
    border-left: 5px solid #16a34a;
    border-radius: 10px;
    color: #1a1a1a !important;
}
.stInfo {
    background: #fef9c3;
    border-left: 5px solid #facc15;
    border-radius: 10px;
    color: #1a1a1a !important;
}
.stWarning {
    background: #fed7aa;
    border-left: 5px solid #fb923c;
    border-radius: 10px;
    color: #1a1a1a !important;
}

/* Markdown text */
.markdown-text-container {
    color: #1a1a1a !important;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #16a34a !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_models():
    scaler = joblib.load("rfm_scaler.joblib")
    kmeans = joblib.load("rfm_kmeans_k2.joblib")
    return scaler, kmeans

scaler, kmeans = load_models()

# =========================================================
# HERO HEADER
# =========================================================

st.markdown("""
<div class="retail-hero">
    <div class="hero-left">
        <div class="hero-icon">🛒</div>
        <div>
            <div class="hero-title">Retail Radar Pro</div>
            <div class="hero-sub">Advanced Customer Segmentation Engine · RFM Analysis · K-Means Clustering</div>
            <div>
                <span class="hero-tag">📊 100K+ Transactions</span>
                <span class="hero-tag">🎯 2-Cluster Segmentation</span>
                <span class="hero-tag">💰 Revenue Intelligence</span>
            </div>
        </div>
    </div>
    <div class="hero-badge">
        ML-Powered<br/>
        Customer Analytics
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown("### 🎯 How It Works")
    st.markdown("""
**Retail Radar Pro** analyzes customer transaction patterns using:

**1️⃣ RFM Analysis**
- Recency (days since last purchase)
- Frequency (# of transactions)
- Monetary (total spend)

**2️⃣ K-Means Clustering**
- Segments customers into groups
- Identifies high-value vs low-value

**3️⃣ Actionable Insights**
- Target marketing campaigns
- Retention strategies
- Revenue optimization
    """)
    
    st.markdown("---")
    st.markdown('<div class="sidebar-section">📂 Sample Dataset</div>', unsafe_allow_html=True)
    st.info("Download the sample CSV below to test the app!")

# =========================================================
# MAIN CONTENT
# =========================================================

st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
st.markdown('<div class="panel-title">📤 Upload Transaction Data</div>', unsafe_allow_html=True)
st.markdown('<div class="panel-sub">Required columns: customer_id, invoice_date, quantity, price (or unit_price)</div>', unsafe_allow_html=True)

# Create two columns for download + upload
upload_col1, upload_col2 = st.columns([1, 2])

with upload_col1:
    st.markdown("**📥 Download Sample Dataset**")
    
    # Create sample data on the fly
    @st.cache_data
    def generate_sample_csv():
        np.random.seed(42)
        n_rows = 2000
        
        sample_data = {
            'customer_id': np.random.randint(1000, 1500, n_rows),
            'invoice_id': [f'INV{i:05d}' for i in range(n_rows)],
            'invoice_date': pd.date_range('2023-01-01', periods=n_rows, freq='3H'),
            'quantity': np.random.randint(1, 15, n_rows),
            'price': np.random.uniform(10, 150, n_rows).round(2)
        }
        return pd.DataFrame(sample_data)
    
    sample_df = generate_sample_csv()
    csv_bytes = sample_df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="⬇️ Download Sample CSV",
        data=csv_bytes,
        file_name="sample_retail_data.csv",
        mime="text/csv",
        use_container_width=True
    )
    
    st.caption("💡 Use this to test the app!")

with upload_col2:
    st.markdown("**📂 Upload Your CSV File**")
    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"],
        label_visibility="collapsed"
    )

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# PROCESS UPLOADED FILE
# =========================================================

if uploaded_file is not None:
    
    with st.spinner("🔄 Processing transaction data..."):
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"❌ Could not read CSV: {e}")
            st.stop()
    
    # Show file info
    st.success(f"✅ Successfully loaded: **{uploaded_file.name}** ({len(df):,} rows)")
    
    # =========================================================
    # DATA PREVIEW
    # =========================================================
    
    st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">👀 Raw Data Preview</div>', unsafe_allow_html=True)
    
    prev_col1, prev_col2, prev_col3, prev_col4 = st.columns(4)
    prev_col1.metric("Total Rows", f"{len(df):,}")
    prev_col2.metric("Columns", len(df.columns))
    prev_col3.metric("Customers", df.iloc[:, 0].nunique() if len(df) > 0 else 0)
    
    # Fixed date range metric
    try:
        date_col = pd.to_datetime(df.iloc[:, 1], errors='coerce')
        date_min = date_col.dropna().min()
        date_range = date_min.strftime('%Y-%m') if not pd.isna(date_min) else 'N/A'
    except:
        date_range = 'N/A'
    prev_col4.metric("Date Range", date_range)
    
    with st.expander("📋 View First 10 Rows"):
        st.dataframe(df.head(10), use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # =========================================================
    # DATA CLEANING & RFM CALCULATION
    # =========================================================
    
    # Standardize columns
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    if "unit_price" in df.columns and "price" not in df.columns:
        df = df.rename(columns={"unit_price": "price"})
    
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], errors='coerce')
    df = df.dropna(subset=["customer_id", "invoice_date"])
    df = df[(df["quantity"] > 0) & (df["price"] > 0)]
    df["total_price"] = df["quantity"] * df["price"]
    
    # RFM calculation
    ref_date = df["invoice_date"].max()
    
    rfm = (
        df.groupby("customer_id")
          .agg({
              "invoice_date": lambda x: (ref_date - x.max()).days,
              "invoice_id": "nunique" if "invoice_id" in df.columns else "count",
              "total_price": "sum"
          })
    )
    rfm.columns = ["recency", "frequency", "monetary"]
    
    # Scale & predict
    rfm_scaled = scaler.transform(rfm[["recency", "frequency", "monetary"]])
    clusters = kmeans.predict(rfm_scaled)
    rfm["cluster"] = clusters
    
    # Map segments
    segment_map = {0: "Low-Value", 1: "High-Value"}
    rfm["segment"] = rfm["cluster"].map(segment_map)
    
    # =========================================================
    # SEGMENTATION RESULTS
    # =========================================================
    
    st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">🎯 Customer Segmentation Results</div>', unsafe_allow_html=True)
    
    seg_col1, seg_col2, seg_col3, seg_col4 = st.columns(4)
    
    total_customers = len(rfm)
    high_value_count = (rfm["segment"] == "High-Value").sum()
    low_value_count = (rfm["segment"] == "Low-Value").sum()
    high_value_pct = (high_value_count / total_customers * 100) if total_customers > 0 else 0
    
    seg_col1.metric("Total Customers", f"{total_customers:,}")
    seg_col2.metric("High-Value", f"{high_value_count:,}", delta=f"{high_value_pct:.1f}%")
    seg_col3.metric("Low-Value", f"{low_value_count:,}")
    seg_col4.metric("Avg Monetary", f"${rfm['monetary'].mean():,.0f}")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # =========================================================
    # VISUALIZATIONS
    # =========================================================
    
    vis_col1, vis_col2 = st.columns(2)
    
    with vis_col1:
        st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
        st.markdown("**📊 Segment Distribution**")
        
        segment_counts = rfm["segment"].value_counts()
        fig = go.Figure(data=[go.Pie(
            labels=segment_counts.index,
            values=segment_counts.values,
            hole=0.5,
            marker=dict(colors=['#16a34a', '#facc15']),
            textinfo='label+percent',
            textfont=dict(size=15, color='#1a1a1a', family='Raleway', weight=700)
        )])
        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with vis_col2:
        st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
        st.markdown("**💰 Revenue by Segment**")
        
        segment_revenue = rfm.groupby("segment")["monetary"].sum().reset_index()
        fig = go.Figure(data=[go.Bar(
            x=segment_revenue["segment"],
            y=segment_revenue["monetary"],
            marker=dict(color=['#16a34a', '#facc15'], line=dict(color='#166534', width=2)),
            text=segment_revenue["monetary"].apply(lambda x: f"${x/1000:.0f}K"),
            textposition='outside',
            textfont=dict(size=14, color='#1a1a1a', family='Raleway', weight=700)
        )])
        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(254,249,195,0.3)',
            xaxis=dict(title='Segment', gridcolor='rgba(34,197,94,0.2)', title_font=dict(color='#1a1a1a', weight=700)),
            yaxis=dict(title='Total Revenue ($)', gridcolor='rgba(34,197,94,0.2)', title_font=dict(color='#1a1a1a', weight=700)),
            showlegend=False,
            font=dict(color='#1a1a1a')
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # =========================================================
    # RFM STATISTICS TABLE
    # =========================================================
    
    st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">📈 Segment RFM Statistics</div>', unsafe_allow_html=True)
    
    rfm_stats = rfm.groupby("segment")[["recency", "frequency", "monetary"]].agg(['mean', 'median', 'std']).round(2)
    st.dataframe(rfm_stats, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # =========================================================
    # 3D SCATTER PLOT
    # =========================================================
    
    st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">🎨 3D RFM Cluster Visualization</div>', unsafe_allow_html=True)
    
    # Sample for performance
    rfm_sample = rfm.sample(n=min(5000, len(rfm)), random_state=42)
    
    fig = px.scatter_3d(
        rfm_sample,
        x='recency',
        y='frequency',
        z='monetary',
        color='segment',
        color_discrete_map={'High-Value': '#16a34a', 'Low-Value': '#facc15'},
        opacity=0.7,
        size_max=8
    )
    fig.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        scene=dict(
            xaxis=dict(title='Recency (days)', backgroundcolor='rgba(254,249,195,0.5)', gridcolor='rgba(34,197,94,0.3)', title_font=dict(color='#1a1a1a')),
            yaxis=dict(title='Frequency', backgroundcolor='rgba(254,249,195,0.5)', gridcolor='rgba(34,197,94,0.3)', title_font=dict(color='#1a1a1a')),
            zaxis=dict(title='Monetary ($)', backgroundcolor='rgba(254,249,195,0.5)', gridcolor='rgba(34,197,94,0.3)', title_font=dict(color='#1a1a1a'))
        ),
        font=dict(color='#1a1a1a')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # =========================================================
    # DOWNLOAD RESULTS
    # =========================================================
    
    st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">💾 Export Segmented Customer Data</div>', unsafe_allow_html=True)
    
    rfm_export = rfm.reset_index()
    csv_export = rfm_export.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="⬇️ Download Customer Segments CSV",
        data=csv_export,
        file_name="customer_segments.csv",
        mime="text/csv"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # =========================================================
    # INITIAL STATE
    # =========================================================
    
    st.markdown('<div class="retail-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">🚀 Get Started</div>', unsafe_allow_html=True)
    
    st.info("""
### 📋 How to Use:

**1️⃣ Download** the sample CSV file from the left section  
**2️⃣ Upload** the CSV (or your own transaction data)  
**3️⃣ Analyze** instant customer segmentation results  
**4️⃣ Export** segmented customer list for campaigns

**Expected CSV Format:**
- `customer_id`: Unique customer identifier
- `invoice_date`: Transaction date (YYYY-MM-DD)
- `quantity`: Items purchased
- `price` or `unit_price`: Price per item
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<hr style="margin-top:2.5rem; border-color:#22c55e; border-width: 2px;">
<div style="text-align:center; padding:1rem 0; color:#166534; font-size:0.85rem;">
    <div style="margin-bottom:6px; color:#15803d; font-weight:600;">
        © 2025 Retail Radar Pro · ML-Powered Customer Segmentation · Built by <span style="color:#166534; font-weight:800;">Mayank Goyal</span>
    </div>
    <div>
        <a href="https://linkedin.com/in/mayank-goyal09" target="_blank"
           style="color:#16a34a; text-decoration:none; margin-right:18px; font-weight:700;">
            🔗 LinkedIn
        </a>
        <a href="https://github.com/mayank-goyal09" target="_blank"
           style="color:#16a34a; text-decoration:none; font-weight:700;">
            💻 GitHub
        </a>
    </div>
    <div style="margin-top:8px; font-size:0.78rem; color:#15803d; font-weight:500;">
        🛒 RFM Analysis · K-Means Clustering · Customer Intelligence
    </div>
</div>
""", unsafe_allow_html=True)
