from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configurations
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# Import routes
from routes.auth_routes import auth_bp
from routes.data_routes import data_bp

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(data_bp)


if __name__ == "__main__":
    app.run(debug=True)

