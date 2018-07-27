[![Build Status](https://travis-ci.org/kcharles52/myDiary.svg?branch=develop)](https://travis-ci.org/kcharles52/myDiary) [![Coverage Status](https://coveralls.io/repos/github/kcharles52/myDiary/badge.svg?branch=develop)](https://coveralls.io/github/kcharles52/myDiary?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/20e34091cd534613516c/maintainability)](https://codeclimate.com/github/kcharles52/myDiary/maintainability)
# MyDiary
This is an online application that helps users to record their memories.


## Prerequisites
* Text editor
* Browser 
* Python/Flask framework

## How to setup the project
* Create a virtual environment using the following command
  > `$python3 -m venv myenv`
* Activate the virtual environment 
  > `$source myenv/bin/activate`
* Install dependencies in the virtual environment
  > `$pip install -r requirements.txt`

##  Run the application
* Use this command to run the application
  > `$python3 run.py`
* View a sample endpoint at http://127.0.0.1:5000/api/v1/register
* You can test the Endpoints with PostMan

## Testing frame works
* nosetests
* pytest
## How to run the tests
* use the following command to run tests
  > `$nosetests --with-coverage`


## Features
### User interface
* signup page
* signin page
* Diary entries
* Diary entry
* Add and modify entry
* Profile page
* Dashboard page

Preview on <a href="https://kcharles52.github.io/myDiary/UI/">Github pages</a>

## Endpoints 
HTTP Method|End point |Action
-----------|----------|--------------
POST | /api/v1/signup | Register a user
POST | /api/v1/login | Login a user
GET| /api/v1/entries   | Fetch all entries
GET | /api/v1/entry/<entry_Id> | Fetch a single entry
POST | /api/v1/entry | Create an entry
PUT | /api/v1/entries/<entry_id>/ | Modify entry

##  Technologies
* HTML
* CSS
* javascript
* Python 3.6

## Author
[Kato Charles](https://github.com/kcharles52)

