from flask import Blueprint, request, jsonify
from ml.anomaly_detector import detect_anomalies

data_bp = Blueprint('data', __name__)

# Endpoint to analyze user behavior
@data_bp.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json.get('activity_data')
    anomalies = detect_anomalies(data)
    #return jsonify({"anomalies": anomalies})
    return "analyze endpoint working"