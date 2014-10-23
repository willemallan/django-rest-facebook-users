# -*- coding: utf-8 -*-
import requests, json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from clients.models import Client
from clients.serializers import ClientSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def client_list(request):
    """
    List all code clients, or create a new client.
    """
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        facebook_id = request.POST.get('facebook_id')
        r = requests.get('http://graph.facebook.com/{0}'.format(facebook_id))
        if r.status_code == 200:
            data = json.loads(r.content)

            if not Client.objects.filter(facebook_id=data['id']):
                client, created = Client.objects.create(
                    facebook_id=data['id'], 
                    username=data['username'],
                    name='{0} {1}'.format(data['first_name'], data['last_name']),
                    gender=data['gender']
                )
                # return HttpResponse(client)
                if created:
                    return JSONResponse(client, status=201)
            return JSONResponse('facebook_id already exists', status=500)

        return JSONResponse('facebook_id not found', status=404)

@csrf_exempt
def client_detail(request, pk):
    """
    Retrieve, update or delete a code client.
    """
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClientSerializer(client, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        client.delete()
        return HttpResponse(status=204)