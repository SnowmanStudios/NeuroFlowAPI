#!flask/bin/python
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)
users = {
	"John123": {
		"password": "123",
		"mood": ["happy", "sad"],
		"startDate": datetime.datetime(2020, 7, 19).strftime('%m/%d/%Y'),
		"lastUpdatedDate": datetime.datetime(2020, 7, 20).strftime('%m/%d/%Y'),
		"streak": 2
	},

	"Sally456": {
		"password": "456",
		"mood": ["hungry", "sad", "tired"],
		"startDate": datetime.datetime(2020, 7, 16).strftime('%m/%d/%Y'),
		"lastUpdatedDate": datetime.datetime(2020, 7, 18).strftime('%m/%d/%Y'),
		"streak": 3
	}
}

@app.route('/mood', methods = ['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		if request.json["username"] in users:
			if request.json["password"] == users[request.json["username"]]["password"]:
				if (datetime.date.today() - datetime.datetime.strptime(users[request.json["username"]]["lastUpdatedDate"], '%m/%d/%Y').date()).days > 1:
					users[request.json["username"]]["startDate"] = datetime.date.today().strftime('%m/%d/%Y')
					users[request.json["username"]]["lastUpdatedDate"] = datetime.date.today().strftime('%m/%d/%Y')
					users[request.json["username"]]["streak"] = 1
				else:
					users[request.json["username"]]["lastUpdatedDate"] = datetime.date.today().strftime('%m/%d/%Y')
					users[request.json["username"]]["streak"] += 1

				users[request.json["username"]]["mood"].append(request.json["newMood"])
				return jsonify({"Updated mood": request.json["newMood"]})
			else:
				return jsonify({"Error": "Incorrect password."})

		else :
			users[request.json["username"]] = {
			"password": request.json["password"],
			"mood": [request.json["newMood"]],
			"startDate": datetime.date.today().strftime('%m/%d/%Y'),
			"lastUpdatedDate": datetime.date.today().strftime('%m/%d/%Y'),
			"streak": 1
			}

			print(users)

			return jsonify({'Created user': request.json["username"]})
	else:
		if request.json["username"] in users:
			if request.json["password"] == users[request.json["username"]]["password"]:
				return jsonify({"All your moods": users[request.json["username"]]["mood"], 
					"Current mood": users[request.json["username"]]["mood"][-1],
					"Current streak": users[request.json["username"]]["streak"]})
			else:
				return jsonify({"Error": "Incorrect password."})
		else:
			return jsonify({"Error": "Please make an account."})

if __name__ == '__main__':
    app.run(debug=True)