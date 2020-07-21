#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
	"John123": {
		"password": "123",
		"mood": ["happy"]
	}
}

@app.route('/mood', methods = ['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		if request.json["username"] in users:
			if request.json["password"] == users[request.json["username"]]["password"]:
				users[request.json["username"]]["mood"].append(request.json["newMood"])
				return jsonify({"Updated mood": request.json["newMood"]})
		
		else :
			users[request.json["username"]] = {
			"password": request.json["password"],
			"mood": [request.json["newMood"]]
			}

			return jsonify({'Created user': request.json["username"]})
	else:
		if request.json["username"] in users:
			if request.json["password"] == users[request.json["username"]]["password"]:
				return jsonify({"All your moods": users[request.json["username"]]["mood"]})
			else:
				return jsonify({"Error": "Incorrect password."})
		else:
			return jsonify({"Error": "Please make an account."})
		return jsonify({"Current user": users})

if __name__ == '__main__':
    app.run(debug=True)