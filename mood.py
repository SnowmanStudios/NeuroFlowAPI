#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)
moods = []

@app.route('/mood', methods = ['GET', 'POST'])
def index():

	if (request.method == 'POST'):
		moodValue = request.json["newMood"]
		moods.append(moodValue)
		return jsonify({'Set mood to': moodValue})
	else:
		if len(moods) == 0:
			return "No moods, add one."
		return jsonify({"Current mood": moods[-1]})

if __name__ == '__main__':
    app.run(debug=True)