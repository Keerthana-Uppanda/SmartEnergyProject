---

# 🔌 Smart Energy Consumption Analysis — House 1 (REFIT Dataset)

This project presents a **data-driven smart energy analysis and visualization system** using the
**REFIT Smart Home Dataset (House 1)**.

The work focuses on **real household energy insights**, combining:

* large-scale time-series data analysis
* appliance-level consumption breakdown
* baseline forecasting concepts
* and a **Flask-based interactive dashboard** for visualization, comparison, and prediction.

---

## 📌 Project Objectives

* Analyze household energy consumption at **appliance level**
* Clean and preprocess large-scale time-series energy data
* Engineer meaningful features from temporal energy patterns
* Build and evaluate a **baseline Linear Regression model**
* Explore deep learning concepts using **LSTM**
* Detect overfitting using **time-series cross-validation**
* Develop a **Flask-based dashboard** for:

  * energy insights
  * appliance comparison
  * future consumption estimation
  * energy-saving recommendations

---

## 📁 Project Structure

```
SmartEnergyProject/
│
├── data/
│   ├── House_1_cleaned_named.csv   # cleaned dataset with real appliance names
│   └── README.md                   # dataset description
│
├── notebooks/
│   ├── 01_Data_Analysis.ipynb        # EDA + preprocessing
│   ├── 02_Feature_Engineering.ipynb  # feature extraction
│   ├── 03_Baseline_Model.ipynb       # linear regression + CV
│   ├── 04_LSTM_Model.ipynb           # LSTM experimentation
│   └── 05_Dashboard_Visualization.ipynb
│
├── app.py                            # Flask backend
│
├── templates/
│   ├── index.html                   # dashboard page
│   ├── predict.html                 # prediction portal
│   └── compare.html                 # appliance comparison
│
├── static/
│   └── style.css                    # UI styling
│
└── README.md
```

---

## 🧹 Module 1 & 2: Data Cleaning and Preprocessing

### Performed Tasks

* Loaded REFIT House 1 dataset (~6.9 million rows)
* Verified data quality:

  * No missing values
  * No duplicate records
* Renamed appliance columns to **real appliance names**:

  * Fridge, Freezer, Washing Machine, Dishwasher, etc.
* Identified outliers and retained them as valid high-energy events
* Converted timestamps to `datetime`
* Set time column as index for time-series analysis
* Created `active_count` feature (number of active appliances)
* Filtered rows with **active_count ≥ 3**
* Resampled energy usage:

  * Hourly
  * Daily
* Normalized data using **Min-Max Scaling**
* Split dataset into:

  * Training (70%)
  * Validation (15%)
  * Testing (15%)

---

## 📊 Module 1: Exploratory Data Analysis (EDA)

### Analysis Included

* Summary statistics for aggregate and appliance-level consumption
* Distribution plots for:

  * Aggregate load
  * Individual appliances
* Boxplots for outlier inspection
* Correlation heatmap showing relationship between appliances and total load

All analysis is documented inside the notebook with plots and tables.

---

## 🧠 Module 3: Feature Engineering

### Features Created

* **Time-based features**

  * Hour
  * Day
  * Weekday
  * Month
* **Appliance aggregation features**

  * Total appliance load
  * Mean appliance load
  * Maximum appliance load
* **Lag features**

  * Previous hour (`lag1`)
  * Previous day (`lag24`)
* **Rolling statistics**

  * 3-hour rolling mean
  * 24-hour rolling mean
* Removed NaN values caused by lag and rolling windows

Final dataset:

* **3702 samples**
* **21 engineered features**
* **1 target variable (aggregate energy consumption)**

---

## 📈 Module 4: Baseline Model Development

### Model Used

* **Linear Regression** as baseline forecasting model

### Evaluation Metrics

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

### Overfitting Check

* Applied **TimeSeriesSplit cross-validation**
* Maintained temporal ordering of data
* Observed consistent MAE values across folds
* Concluded that the baseline model **does not suffer from overfitting**

---

## 🤖 Module 5: LSTM Model (Exploratory)

### Purpose

* To understand deep learning approaches for time-series forecasting
* To compare classical ML with neural network models

### Highlights

* Implemented LSTM with a 24-hour lookback window
* Trained using Adam optimizer and MSE loss
* Evaluated using MAE, RMSE, and R² score
* Used primarily as a **conceptual extension**, not the core deployment model

---

## 🔗 Module 6: Model Evaluation and Integration

* Compared Linear Regression and LSTM models
* Evaluated both using:

  * MAE
  * RMSE
  * R² score
* Used evaluation results to guide deployment decisions
* Prepared model logic for integration into Flask backend

---

## 🖥️ Module 7: Dashboard and Visualization (Flask Application)

### Dashboard Capabilities

* Built a **Flask-based web dashboard**
* Displays **real energy insights from actual data**
* Visualizations include:

  * Hourly energy consumption (bar chart)
  * Appliance-wise energy distribution (pie chart)
* Appliance comparison portal for identifying top consumers
* Prediction portal for:

  * next hours
  * next day
  * next week
  * next two months (trend-based estimation)

### Smart Insights

* Identifies:

  * Top energy-consuming appliance
  * Peak usage hour
* Provides **energy-saving recommendations**

  * Especially for **Washing Machine**, including:

    * off-peak usage
    * full-load operation
    * eco mode suggestions
* Displays **estimated energy savings (15–25%)** based on optimized usage patterns

---

## 🗂 Dataset Information

* **Dataset:** REFIT Smart Home Energy Dataset — House 1
* **Original size:** ~6.9 million rows
* **After filtering:** ~2.7 million rows
* **Final uploaded version:** cleaned and reduced for GitHub compatibility

---

## 🚀 Future Work

* Appliance-specific prediction models
* Advanced forecasting techniques
* Cloud deployment of the dashboard
* User authentication and personalization
* Automated energy-saving recommendation engine

---

## 👤 Author

**Uppanda Keerthana**
Smart Energy Consumption Project

---

