from rest_framework.test import APIClient

client = APIClient()
client.post('/clients/', {'facebook_id': '123'}, format='json')
client.get('/clients/', {}, format='json')
client.get('/clients/123/', {}, format='json')
client.get('/clients/?limit=1', {}, format='json')
client.delete('/clients/123/', {}, format='json')

# from rest_framework.test import APIRequestFactory

# # Using the standard RequestFactory API to create a form POST request
# factory = APIRequestFactory()
# request = factory.post('/clients/', {'facebook_id': '123'}, format='json')
# request = factory.get('/clients/', {}, format='json')
# request = factory.get('/clients/123/', {}, format='json')
# request = factory.get('/clients/?limit=1', {}, format='json')
# request = factory.delete('/clients/123/', {}, format='json')