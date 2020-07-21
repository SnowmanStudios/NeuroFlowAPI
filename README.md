# NeuroFlowAPI
"Mood Tracker" for NeuroFlow Co-op Assessment.

## Getting Started
### Prerequisites
This project needs Python, Flask 1.1.x, and Werkzeug 0.16.1

If needed:
[Install Python](https://www.python.org/downloads/)
[Install pip](https://pip.pypa.io/en/stable/installing/)
```
pip3 install -r requirements.txt
```
### Download
Download the mood.py file by going to https://raw.githubusercontent.com/SnowmanStudios/NeuroFlowAPI/master/mood.py and save the page as mood.py or in the terminal the follow where you want the file to go:
```
curl -LJO https://raw.githubusercontent.com/SnowmanStudios/NeuroFlowAPI/master/mood.py
```

### How to use
Run the file in one terminal,
```
python3 mood.py
```
and use a second ternimal to send GET and POST requests.

For a GET request, copy and paste the following curl command into the terminal (change the username and password values for a specific account).
```
curl -X GET \ 
  -H "Content-type: application/json" \
  -H "Accept: application/json" \                                       
  -d '{"username":"Sam123", "password": "0000"}' \
  "http://127.0.0.1:5000/mood"
```
For a POST request, copy and paste the following curl command into the terminal (change the username, password, and newMood values for a specific account). If the username already exists, the newMood will be appended to the users mood list.
```
curl -X POST \
  -H "Content-type: application/json" \
  -d '{"username":"Sally456", "password": "456", "newMood": "happy"}' \
  http://127.0.0.1:5000/mood 
```
## Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Acknowledgements
* [Original Flask code from Melvin L.](https://www.youtube.com/watch?v=s_ht4AKnWZg)

## Reflection
This is my first time working with Flask and using Python for anything server related. I apologize for the horrendous code. 

Since I worked on this assessment for an elapsed time of approximately 24 hours, I can safetly say that I would change just about everything if I had more time. If something worked, I felt it as is.

If this were an actual production application, I would communicate with the product owner regarding specific front and back-end requirements. I would make an interface of some sort for GET, POST, and user login. I would also verify that all parts of the GET, POST, and user login were inputted.

The whole /mood route is one big if else statement with multiple levels of if else statements inside. Rather than comparing password string I would've hashed the passwords for security. I quickly realized when implementing a type of user login I should've made User objects and put them in a database instead of putting all the information in a local JSON body.