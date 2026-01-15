```markdown
# 🔌 Smart Energy Consumption Analysis — House 1 (REFIT Dataset)

This project presents an end-to-end **energy consumption analysis and forecasting system** using the **REFIT Smart Home Dataset (House 1)**.
The work spans from **raw data preprocessing** to **deep learning–based time-series forecasting** and **deployment-ready model integration using Flask**.

---

## 📌 Project Objectives

- Analyze household energy consumption at appliance level
- Clean and preprocess large-scale time-series energy data
- Engineer meaningful features for forecasting
- Build and evaluate a **baseline Linear Regression model**
- Develop an **LSTM-based deep learning model**
- Evaluate models using standard metrics and detect overfitting
- Deploy the trained model using a **Flask-based web dashboard**

---

## 📁 Project Structure

SmartEnergyProject/
│
├── data/
│   ├── House_1_cleaned_named.csv
│   └── README.md
│
├── notebooks/
│   ├── 01_Data_Analysis.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Baseline_Model.ipynb
│   ├── 04_LSTM_Model.ipynb
│   └── 05_Dashboard_Visualization.ipynb
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
├── static/
│   └── style.css


---

## 🧹 Module 1 & 2: Data Cleaning and Preprocessing

### Performed Tasks

- Loaded REFIT House 1 dataset (~6.9 million rows)
- Verified data quality:
  - No missing values
  - No duplicate records
- Renamed appliance columns to **meaningful appliance names**
- Identified outliers and retained them as valid high-energy events
- Converted timestamps to `datetime` format
- Set time as the index for time-series analysis
- Created an `active_count` feature representing the number of active appliances
- Filtered rows with **active_count ≥ 3** to focus on meaningful consumption periods
- Resampled data:
  - Hourly
  - Daily
- Normalized features using **Min-Max Scaling**
- Split dataset into:
  - Training set (70%)
  - Validation set (15%)
  - Test set (15%)

---

## 📊 Module 1: Exploratory Data Analysis (EDA)

### Analysis Included

- Summary statistics of aggregate and appliance-level consumption
- Distribution plots for:
  - Aggregate energy usage
  - Individual appliances
- Boxplots for outlier inspection
- Correlation heatmap illustrating relationships between appliances and total energy consumption

All tables and visualizations are included directly inside the notebook.

---

## 🧠 Module 3: Feature Engineering

### Features Created

- **Time-based features**
  - Hour
  - Day
  - Weekday
  - Month
- **Device-level aggregation features**
  - Total appliance load
  - Mean appliance load
  - Maximum appliance load
- **Lag features**
  - Previous hour (`lag1`)
  - Previous day (`lag24`)
- **Rolling statistics**
  - 3-hour rolling mean
  - 24-hour rolling mean
- Removed NaN values introduced by lag and rolling operations
- Prepared final machine-learning-ready dataset

Final dataset characteristics:
- **3702 samples**
- **21 engineered features**
- **1 target variable (aggregate energy consumption)**

---

## 📈 Module 4: Baseline Model Development

### Model Implemented

- **Linear Regression** as a baseline forecasting model

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Metrics were calculated for training, validation, and test sets.

### Time-Series Cross-Validation (Overfitting Check)

- Applied **TimeSeriesSplit cross-validation** to preserve temporal ordering
- Observed consistent MAE values across folds with low variance
- Results indicate that the baseline model **does not suffer from overfitting**

---

## 🤖 Module 5: LSTM Model Development

### Model Design

- Implemented an **LSTM (Long Short-Term Memory)** network using TensorFlow/Keras
- Used sequential input with a **24-hour lookback window**
- Architecture:
  - LSTM layer with 64 units
  - Dropout layer for regularization
  - Dense output layer for regression

### Training and Evaluation

- Trained using Adam optimizer and Mean Squared Error loss
- Evaluated using MAE, RMSE, and R² score
- Compared LSTM with Linear Regression on identical test data

---

## 🔗 Module 6: Model Evaluation and Integration

### Model Evaluation

- Evaluated both models using:
  - MAE
  - RMSE
  - R² score
- Selected the best-performing model based on evaluation results

### Model Saving & Integration

- Saved the final LSTM model in **native `.keras` format**
- Implemented a **Flask-compatible prediction function**
- Verified model predictions using sample inputs prior to deployment

---

## 🖥️ Module 7: Dashboard and Visualization (Flask)

### Dashboard Features

- Developed a **Flask-based web application** (`app.py`) for model inference
- Integrated the trained LSTM model into the Flask backend
- Automatically constructs appliance-specific input sequences using recent historical data
- Implemented **multi-step future forecasting** (6, 12, and 24 hours)
- Designed a clean and responsive dashboard using **HTML and CSS**
- Visualized predictions using **interactive line charts (Chart.js)**

### Purpose

This module enables:
- Real-time model interaction
- Demonstration-ready deployment
- Clear visualization of future energy consumption trends per appliance

---

## 🗂 Dataset Information

- **Dataset:** REFIT Smart Home Energy Dataset — House 1
- **Original size:** ~6.9 million rows
- **After filtering (active_count ≥ 3):** ~2.7 million rows
- **Uploaded version:** Cleaned and reduced dataset to comply with GitHub size limits

---

## 🚀 Future Work

- Appliance-specific forecasting models
- Advanced LSTM architectures (stacked / bidirectional)
- Hyperparameter optimization using grid or random search
- Cloud deployment of the Flask application
- Smart energy usage recommendation system

---

## 👤 Author

**Uppanda Keerthana**  
B.Tech — Computer Science Engineering  
Smart Energy Consumption Project
```

