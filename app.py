from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()

    full_name = "Tejus_Cherian_Sujith"
    dob = "13022003"
    user_id = f"{full_name}_{dob}"

    if "data" not in data or not isinstance(data["data"], list):
        return jsonify({
            "is_success": False,
            "user_id": user_id,
            "message": "Invalid data format"
        }), 400

    numbers = [item for item in data["data"] if item.isdigit()]
    alphabets = [item for item in data["data"] if item.isalpha()]
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase = max(lowercase_alphabets, default=None)

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": "tejus.sujith@gmail.com",
        "roll_number": "21BCB0008",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
    }

    return jsonify(response), 200

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
