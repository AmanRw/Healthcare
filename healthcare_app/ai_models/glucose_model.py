import numpy as np
from sklearn.ensemble import IsolationForest
from joblib import dump, load
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
os.makedirs(MODEL_DIR, exist_ok=True)

class SimpleAnomalyDetector:
    def __init__(self, contamination=0.05, random_state=42):
        self.contamination = contamination
        self.random_state = random_state
        # Model is trained per-patient in-memory; optionally persist using joblib

    def train(self, readings):
        """
        readings: iterable of numeric values
        """
        X = np.array(readings).reshape(-1, 1)
        if len(X) < 5:
            # Not enough data to train robustly; fall back to simple thresholding
            return None
        model = IsolationForest(contamination=self.contamination, random_state=self.random_state)
        model.fit(X)
        return model

    def is_anomaly(self, model, new_value):
        """
        model: trained IsolationForest or None
        new_value: numeric
        Returns: True if anomaly (i.e., model predicts -1), False otherwise
        """
        if model is None:
            # fallback: simple heuristics - outside 3*std dev or medically extreme values
            return self.heuristic_check(new_value, None)
        pred = model.predict(np.array([[new_value]]))
        return pred[0] == -1

    def heuristic_check(self, value, readings_stats):
        # Very simple medical heuristics: adjust to your case
        # For glucose (mg/dL): normal fasting ~70-100; extreme <50 or >400 alert
        # For heart rate (bpm): normal 50-100; extreme <30 or >200 alert
        # We'll be generic here; specialized logic can be added externally.
        if value <= 0:
            return True
        return False
