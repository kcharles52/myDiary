import json
from tests import BaseTestCaseDiaryEntry
from app.views import app


class EntriesTest(BaseTestCaseDiaryEntry):
        #tests for creating diary entry
    def test_create_request(self):
        """ Tests whether a user can create an entry successfully """
        response = self.test_client.post(
            '/api/v1/entries', data=json.dumps(self.diary_entry_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("You have successfully created your entry",str(response.data))

    def test_create_entry_without_title(self):
        """ Tests whether a user can not create an entry without a title """
        response = self.test_client.post('/api/v1/entries', data=json.dumps(
            {"title": "", "date": "2/2/2017", "diaryBody": "Entry without title"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('title is required', str(response.data))

    def test_create_entry_without_date(self):
        """ Tests whether a user can not create an entry without a date """
        response = self.test_client.post('/api/v1/entries', data=json.dumps(
            {"title": "Wed", "date": "", "diaryBody": "Entry without title"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('date is required', str(response.data))

    def test_create_entry_without_body(self):
        """ Tests whether a user can not create an entry without a body """
        response = self.test_client.post('/api/v1/entries', data=json.dumps(
            {"title": "Wed", "date": "", "diaryBody": "Entry without title"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('date is required', str(response.data))
