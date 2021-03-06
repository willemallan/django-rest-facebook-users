# -*- coding: utf-8 -*-
import requests, json
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from clients.models import Client
from clients.serializers import ClientSerializer

def log(name, function, message='', level='INFO'):
    from logs.models import Log
    Log.objects.create(name=name, function=function, message=message, level=level)

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
        limit = int(request.GET.get('limit', 1))
        p = Paginator(Client.objects.all(), 10)
        num_pages = p.num_pages
        if limit <= num_pages:
            page = p.page(limit)
            clients = page.object_list
            log('client_list', 'list', 'list users')
        else:
            return JSONResponse({'erro': 'no more records'})

        serializer = ClientSerializer(clients, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        facebook_id = request.POST.get('facebook_id')
        r = requests.get('http://graph.facebook.com/{0}'.format(facebook_id))
        if r.status_code == 200:
            data = json.loads(r.content)
            print data['id']
            if not Client.objects.filter(facebook_id=data['id']):
                log('client_list', 'new', 'new client %s' % facebook_id)
                facebook_id = data['id']
                username = data['username']
                name = u'{0} {1}'.format(data['first_name'], data['last_name'])
                gender = data['gender']

                client = Client.objects.create(
                    facebook_id=facebook_id, 
                    username=username,
                    name=name,
                    gender=gender
                )

                client = Client.objects.filter(facebook_id=facebook_id).values('facebook_id', 'username', 'name', 'gender')
                return HttpResponse(client, status=201)

            log('client_list', 'new', 'facebook_id %s already exists' % facebook_id, 'ERROR')
            return JSONResponse('facebook_id already exists', status=500)

        return JSONResponse('facebook_id not found', status=404)

@csrf_exempt
def client_detail(request, facebook_id):
    """
    Retrieve, update or delete a code client.
    """
    try:
        client = Client.objects.get(facebook_id=facebook_id)
    except Client.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        log('client_detail', 'detail', 'detail user %s' % facebook_id)
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
        log('client', 'delete', 'delete client %s' % facebook_id)
        return HttpResponse(status=204)