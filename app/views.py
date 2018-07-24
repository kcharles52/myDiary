from flask import Flask, request, jsonify, make_response
import json
import re
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
