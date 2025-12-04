# Smart Energy Consumption Analysis — House 1 (REFIT Dataset)

This project performs **device-level energy consumption analysis** using the REFIT Smart Home Dataset.  
The work includes:

- Data cleaning  
- Handling nulls and duplicates  
- Outlier detection  
- Summary statistics  
- Distribution plots  
- Correlation heatmap  
- Filtering rows based on appliance activity  
- Preparing cleaned dataset for ML tasks  

This repository will later include:
- Feature engineering  
- Linear Regression baseline model  
- LSTM forecasting model  
- Flask-based dashboard  

---

## 📁 Project Structure

SmartEnergyProject/
│
├── data/
│ ├── House_1_cleaned_sampled.csv # cleaned & sampled dataset for analysis
│ └── README.md # dataset description
│
├── notebooks/
│ └── Data_Analysis_House1.ipynb # Jupyter notebook for EDA
│
├── README.md # project documentation
└── .gitignore # ignore venv and cache files


---

## 🧹 Data Cleaning

Performed:
- Removed rows with **active_count < 3**
- Calculated active appliances per timestamp
- Converted Time column to datetime
- Set Time as index
- Filtered high-activity periods for better analysis

---

## 📊 Exploratory Data Analysis (EDA)

Included:
- Null value check
- Duplicate check
- Data type analysis
- Outlier inspection (boxplots)
- Distribution plots for:
  - Aggregate load
  - Appliance1–Appliance9
- Correlation heatmap:
  Shows relationships between appliances and total aggregate power.

---

## 🗂 Dataset

REFIT Smart Home Energy Dataset — House 1  
Sampling: **1 row per 10** for GitHub upload.

**Original dataset has over 6.9M rows**  
**Cleaned (active_count ≥ 3) has ~2.7M rows**  
**Uploaded sampled dataset has reduced size for GitHub**

---

## 🚀 Next Steps (Week by Week)

- Feature Engineering (lag features, rolling averages)
- Baseline Linear Regression model
- LSTM time-series forecasting
- Model comparison
- Smart suggestions engine
- Flask dashboard integration

---

## 👤 Author

Keerthi (Keerthana-Uppanda)  
BTech — Computer Science Engineering  
Smart Energy Consumption Project

