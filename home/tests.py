# imports
import json
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer


class CustomerTests(APITestCase):
    api_url = "http://127.0.0.1:8000/customer/"
    data = {
        "name": "test customer",
        "email": "test@example.com",
        "phone": "+919999999999",
        "slug": "Test_cust_test",
        "profile": {
            "bio":"this is a test customer",
            "dob":"2020-09-08",
            "git_profile_link":"https://github.com/abhidevx/"
        }
    }
   
    def test_create_customer(self):
        response = self.client.post(self.api_url, self.data, format='json')
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data["name"], 'test customer')
    
    def test_get_customer(self):
        self.client.post(self.api_url, self.data, format='json')
        response = self.client.get(self.api_url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data[0]["name"], 'test customer')
    
    def test_update_customer(self):
        response = self.client.post(self.api_url, self.data, format='json')
        response_data = json.loads(response.content)
        self.data["name"] = "test customer updated"
        response = self.client.put(f'{self.api_url}{response_data["id"]}/', self.data, format='json')
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["name"], 'test customer updated')
        self.assertEqual(response_data["email"], 'test@example.com')

    def test_delete_customer(self):
        response = self.client.post(self.api_url, self.data, format='json')
        response_data = json.loads(response.content)
        response = self.client.delete(f'{self.api_url}{response_data["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
