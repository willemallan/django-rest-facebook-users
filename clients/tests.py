from rest_framework.test import APIClient

client = APIClient()
client.post('/person/', {'facebook_id': '123'})
client.post('/person/', {'facebook_id': '1234'})
client.post('/person/', {'facebook_id': '12345'})
client.post('/person/', {'facebook_id': '123456'})
client.post('/person/', {'facebook_id': '1048721376'})
client.get('/person/', {})
client.get('/person/123/', {})
client.get('/person/?limit=1', {})
client.delete('/person/123/', {})