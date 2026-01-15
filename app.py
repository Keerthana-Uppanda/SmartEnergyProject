from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

# ---------------------------------
# Flask App
# ---------------------------------
app = Flask(__name__)

# ---------------------------------
# Load model & scaler
# ---------------------------------
model = load_model("lstm_energy_model.keras")
scaler = joblib.load("target_scaler.pkl")

# ---------------------------------
# Load cleaned & named dataset
# ---------------------------------
DATA_PATH = "data/House_1_cleaned_named.csv"
df = pd.read_csv(DATA_PATH)

# ---------------------------------
# Appliance list (UI & DATA MATCH)
# ---------------------------------
APPLIANCES = [
    "Fridge",
    "Freezer",
    "Washing_Machine",
    "Dishwasher",
    "Microwave",
    "Kettle",
    "Television",
    "Computer",
    "Lighting"
]

# ---------------------------------
# Feature index map (MUST match training)
# ---------------------------------
FEATURE_INDEX_MAP = {
    "Aggregate": 0,
    "Fridge": 1,
    "Freezer": 2,
    "Washing_Machine": 3,
    "Dishwasher": 4,
    "Microwave": 5,
    "Kettle": 6,
    "Television": 7,
    "Computer": 8,
    "Lighting": 9
}
# Remaining engineered features → indices 10–21 (kept zero)

# ---------------------------------
# Fetch last 24-hour appliance history
# ---------------------------------
def get_last_24_hours(appliance):
    return df[appliance].tail(24).values

# ---------------------------------
# Build appliance-specific LSTM input
# ---------------------------------
def build_input_sequence(appliance):
    seq = np.zeros((24, 22))

    appliance_series = get_last_24_hours(appliance)

    appliance_idx = FEATURE_INDEX_MAP[appliance]

    # Fill appliance column
    seq[:, appliance_idx] = appliance_series

    # Derive aggregate realistically
    seq[:, FEATURE_INDEX_MAP["Aggregate"]] = appliance_series

    return seq

# ---------------------------------
# Multi-step future prediction
# ---------------------------------
def predict_future(sequence_24x22, steps=24):
    future_preds = []
    current_seq = sequence_24x22.copy()

    for _ in range(steps):
        seq = current_seq.reshape(1, 24, 22)
        scaled_pred = model.predict(seq, verbose=0)

        real_pred = float(
            scaler.inverse_transform(scaled_pred)[0][0]
        )
        future_preds.append(round(real_pred, 2))

        next_row = current_seq[-1].copy()
        next_row[FEATURE_INDEX_MAP["Aggregate"]] = scaled_pred[0][0]
        current_seq = np.vstack([current_seq[1:], next_row])

    return future_preds

# ---------------------------------
# Routes
# ---------------------------------
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    future_preds = None
    appliance = None

    if request.method == 'POST':
        appliance = request.form['appliance']
        hours = int(request.form['hours'])

        input_seq = build_input_sequence(appliance)
        future_preds = predict_future(input_seq, steps=hours)

    return render_template(
        "dashboard.html",
        appliances=APPLIANCES,
        appliance=appliance,
        future_preds=future_preds
    )

# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)
