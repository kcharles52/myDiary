import unittest
import pytest

from app.views import app
from app.models import diaryEntries, users

#Base test class for users
class BaseTestCaseUser(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.user_register_data = {
            "name": "Kato",
            "email": "kato@gmail.com",
            "password": "123456"
        }
        self.user_login_data = {
            "email": "kato@gmail.com",
            "password": "123456"
        }

    def tearDown(self):
        users[:]=[]

#Base test class for diary entries
class BaseTestCaseDiaryEntry(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.diary_entry_data={
            "diaryTitle": "wedding Dm",
            "date": "1/2/2017",
            "diaryEntryBody": "This some message for the entry in the diary",
            "entry_id": "1"
        }

    def tearDown(self):
        diaryEntries[:] = []