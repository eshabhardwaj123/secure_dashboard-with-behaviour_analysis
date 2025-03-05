from sklearn.ensemble import IsolationForest
import numpy as np

# Sample Anomaly Detection Model
def detect_anomalies(data):
    model = IsolationForest(contamination=0.2)
    np_data = np.array(data)
    model.fit(np_data)
    predictions = model.predict(np_data)
    return predictions.tolist()
