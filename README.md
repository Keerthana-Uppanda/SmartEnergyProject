🔌 Smart Energy Consumption Analysis — House 1 (REFIT Dataset)

This project presents an end-to-end energy consumption analysis and forecasting system using the REFIT Smart Home Dataset (House 1).
The work spans from raw data preprocessing to deep learning–based time-series forecasting using LSTM.

📌 Project Objectives

Analyze household energy consumption at appliance level

Clean and preprocess large-scale time-series energy data

Engineer meaningful features for forecasting

Build and evaluate a baseline Linear Regression model

Develop an LSTM-based deep learning model

Compare baseline and advanced forecasting models

📁 Project Structure
SmartEnergyProject/
│
├── data/
│   ├── House_1_cleaned_sampled.csv   # cleaned & sampled dataset (EDA reference)
│   └── README.md                     # dataset notes
│
├── notebooks/
│   ├── 01_Data_Analysis.ipynb        # Module 1 & 2: EDA + Preprocessing
│   ├── 02_Feature_Engineering.ipynb  # Module 3: Feature Engineering
│   ├── 03_Baseline_Model.ipynb       # Module 4: Linear Regression baseline
│   └── 04_LSTM_Model.ipynb           # Module 5: LSTM deep learning model
│
├── README.md                         # project documentation
└── .gitignore                        # ignore venv, cache files

🧹 Module 1 & 2: Data Cleaning and Preprocessing
Performed Tasks

Loaded REFIT House 1 dataset (~6.9 million rows)

Verified data quality:

No missing values

No duplicate records

Renamed appliance columns to meaningful appliance names

Identified outliers and retained them as valid high-energy events

Converted timestamps to datetime format

Set time as the index for time-series analysis

Created an active_count feature representing the number of active appliances

Filtered rows with active_count ≥ 3 to focus on meaningful consumption periods

Resampled data:

Hourly

Daily

Normalized features using Min-Max Scaling

Split dataset into:

Training set (70%)

Validation set (15%)

Test set (15%)

📊 Module 1: Exploratory Data Analysis (EDA)
Analysis Included

Summary statistics of aggregate and appliance-level consumption

Distribution plots for:

Aggregate energy usage

Individual appliances

Boxplots for outlier inspection

Correlation heatmap illustrating relationships between appliances and total energy consumption

All tables and visualizations are included directly inside the notebook.

🧠 Module 3: Feature Engineering
Features Created

Time-based features

Hour

Day

Weekday

Month

Device-level aggregation features

Total appliance load

Mean appliance load

Maximum appliance load

Lag features

Previous hour (lag1)

Previous day (lag24)

Rolling statistics

3-hour rolling mean

24-hour rolling mean

Removed NaN values introduced by lag and rolling operations

Prepared final machine-learning-ready dataset

Final dataset characteristics:

3702 samples

21 engineered features

1 target variable (aggregate energy consumption)

📈 Module 4: Baseline Model Development
Model Implemented

Linear Regression as a baseline forecasting model

Evaluation Metrics

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

Metrics were calculated for:

Training set

Validation set

Test set

Visualizations

Actual vs Predicted energy consumption (line plot)

Scatter plot of actual vs predicted values

The baseline model provides a reference for evaluating advanced models.

🤖 Module 5: LSTM Model Development
Model Design

Implemented an LSTM (Long Short-Term Memory) network using TensorFlow/Keras

Used sequential input with a 24-hour lookback window

Model architecture:

LSTM layer with 64 units

Dropout layer for regularization

Dense output layer for regression

Training and Hyperparameter Tuning

Trained using Adam optimizer and Mean Squared Error loss

Experimented with different:

Epoch values

Batch sizes

Selected the configuration based on validation loss convergence

Evaluation and Comparison

Evaluated the LSTM model using:

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

Retrained Linear Regression on the same train-test split for fair comparison

LSTM achieved lower error values than the baseline model, demonstrating improved performance by capturing temporal dependencies

Visualizations

Actual vs Predicted energy usage for the LSTM model

Comparative visualization of:

Linear Regression predictions

LSTM predictions

Actual energy consumption

These visualizations clearly show the LSTM model’s superior ability to follow temporal patterns in energy usage.

🗂 Dataset Information

Dataset: REFIT Smart Home Energy Dataset — House 1

Original size: ~6.9 million rows

After filtering (active_count ≥ 3): ~2.7 million rows

Uploaded version: Sampled dataset to comply with GitHub size limits

🚀 Future Work

Advanced LSTM architectures (stacked and bidirectional LSTM)

Hyperparameter optimization using grid/random search

Model deployment using Flask

Interactive dashboard for energy visualization

Smart energy usage recommendation system

👤 Author

Uppanda Keerthana
B.Tech — Computer Science Engineering
Smart Energy Consumption Project
