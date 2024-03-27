from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://ub:1234@mlopstask5.3dsq8wh.mongodb.net/?retryWrites=true&w=majority&appName=mlopstask5"
mongo = PyMongo(app)

@app.route('/submit', methods=['POST'])
def submit():
    user_info = request.json
    mongo.db.users.insert_one(user_info)
    return jsonify(message="User info saved"), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
