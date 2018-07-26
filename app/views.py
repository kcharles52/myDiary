from flask import Flask, request, jsonify, make_response
import json
import re
from .models import DiaryEntry, diaryEntries

app = Flask(__name__)

#register route
@app.route('/api/v1/users', methods=['POST'])
def register_user():
    #get user data from request
    user_registration_data = request.get_json()

    #check if data has been passed into URL
    if not user_registration_data:
        return jsonify({'Message': 'All fields are required'}), 400

    name = user_registration_data['name']
    email = user_registration_data['email']
    password = user_registration_data['password']

    if not name or name == "" or name == type(int) or len(name) < 3:
        return jsonify({'message': 'Invalid name'}), 400

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return make_response(jsonify({
            "status": "Fail",
            "message": "Enter valid email"}), 400)
    if not password or password == " " or len(password) < 5:
        return jsonify({'message': 'A stronger password  is required'}), 400

    return jsonify({'message': 'User {} has been registered'.format(name)}), 201


#login route
@app.route('/api/v1/user', methods=['POST'])
def login_user():
    # getting user login data
    user_login_data = request.get_json()

    #check if returned user data is empty
    if not user_login_data:
        return jsonify({'Message': 'All fields are required'}), 400

    email = str(user_login_data.get('email')).strip()
    password = user_login_data.get('password').strip()

    if not email or email == " ":
        return jsonify({'Message': 'email is required'}), 400

    if not password or password == " ":
        return jsonify({'Message': 'password  is required'}), 400
    return jsonify({"Message": "Welcome. You are logged in"}), 200

#create entry route

@app.route("/api/v1/entries", methods=["POST"])
def create_entry():
    """ Endpoint to get the diary entry data entered by the user """
    # get request data
    diary_entry_data = request.get_json()

    #check if entry data is not empty
    if not diary_entry_data:
        return jsonify({"message": "Enter data in all fields"}), 400

    diaryTitle = str(diary_entry_data.get('diaryTitle')).strip()
    date = str(diary_entry_data.get('date')).strip()
    diaryEntryBody = diary_entry_data.get('diaryEntryBody')
    entry_id = len(diaryEntries)+1

    # validate request data
    if not diaryTitle or diaryTitle == "" or diaryTitle == type(int):
        return jsonify({'Message': 'Title is required'}), 400
    if not date or date == "":
        return jsonify({'Message': 'date is required'}), 400
    if not diaryEntryBody or diaryEntryBody == "":
        return jsonify({'Message': 'Field required: Please write someting'}), 400

    new_diary_entry = DiaryEntry(diaryTitle, date, diaryEntryBody, entry_id)
    diaryEntries.append(new_diary_entry)

    return jsonify({'Message': 'You have successfully created your entry'}), 201

#route for fetiching all diary entries
@app.route("/api/v1/entries", methods=["GET"])
def fetch_entries():
    if len(diaryEntries) < 1:
        return jsonify({"Message": "You have no entries"}), 404

    if len(diaryEntries) >= 1:
        return jsonify({
            "Message": "Successfully fetched entries",
            "entriess": [
                entry.__dict__ for entry in diaryEntries
            ]
        }), 200

#route for fetching single entry by id
@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def get_single_entry(entry_id):
    """ Endpoint to fetch a single entry """
    if len(diaryEntries) < 1:
        return jsonify({ "Message": "You have no entries"}), 404
    for entry in diaryEntries:
        if entry.entry_id == entry_id:
            return jsonify({'entry': entry.__dict__}), 200
    return jsonify({'Message': 'Diary Entry Not Found'}), 404
