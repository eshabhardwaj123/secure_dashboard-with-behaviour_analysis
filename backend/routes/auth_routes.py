from flask import Blueprint, request, jsonify
import bcrypt
from config import get_db_connection

auth_bp = Blueprint('auth', __name__)

# User Registration
@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password').encode('utf-8')

    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed))
    db.commit()

    #return jsonify({"message": "User registered successfully"})
    return "register endpoint working"
# User Login
@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password').encode('utf-8')

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    #if result and bcrypt.checkpw(password, result[0].encode('utf-8')):
      #  return jsonify({"message": "Login successful"})
   # else:
      #  return jsonify({"message": "Invalid credentials"}), 401
    return "login endpoint working"
    