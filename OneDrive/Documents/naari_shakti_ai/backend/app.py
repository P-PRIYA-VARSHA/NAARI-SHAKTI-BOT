from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
from pymongo import MongoClient
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file (create this file)
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Secure MongoDB Atlas Connection
MONGO_URI = os.getenv("mongodb+srv://ppriyavarsha23:cEW8YecsCPsnHpAu@cluster0.pern1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(MONGO_URI)
db = client["naari_shakti"]
collection = db["emergency_logs"]
recordings_collection = db["recordings"]

# Secure Twilio Credentials
# Twilio credentials (Replace with actual credentials)
TWILIO_ACCOUNT_SID = "ACfccfd79786b9f0330a630a611f8817a5"
TWILIO_AUTH_TOKEN = "4955e4655f6345b260880ef1e7075f1d"
TWILIO_PHONE_NUMBER = "+12705944023"
EMERGENCY_CONTACT = "+917569744503"

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

UPLOAD_FOLDER = os.path.abspath("uploads")  # Absolute path for safety
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    """Root route for testing."""
    return "🚀 Flask Server is Running!"

call = twilio_client.calls.create(
    url="https://handler.twilio.com/twiml/EHb9f28988fac8a25567a597a8bfa8fc1d",
    to="+917569744503",
    from_="+12705944023"
)


'''
@app.route('/emergency', methods=['POST'])
def emergency():
    try:
        data = request.get_json()
        print("Received data:", data)

        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude and longitude:
            message_body = f"🚨 EMERGENCY ALERT! 🚨\nLocation: https://www.google.com/maps?q={latitude},{longitude}"
            
            # Sending SMS via Twilio
            message = twilio_client.messages.create(
                body=message_body,
                from_="+12705944023",
                to="+917569744503"
            )

            print("SMS sent successfully:", message.sid)
            return jsonify({"status": "Emergency alert sent", "message_sid": message.sid}), 200
        else:
            return jsonify({"error": "Invalid location data"}), 400

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/logs", methods=["GET"])
def get_logs():
    logs = list(collection.find({}, {"_id": 0}))  # Exclude `_id`
    return jsonify(logs)

@app.route("/upload", methods=["POST"])
def upload():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)

        # Save metadata to MongoDB
        recordings_collection.insert_one({
            "filename": file.filename,
            "timestamp": datetime.now(),
            "file_path": filename
        })

        return jsonify({"message": "File uploaded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
'''

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Ensure Flask runs on port 5000
