import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from base_connect.models import Person
from django.http import JsonResponse


@csrf_exempt
def home(request):
    if request.GET.get('is') == 'online':  # http://127.0.0.1:8000/?is=online
        print('online')
        return HttpResponse('True')
    else:
        print('offline')
        return HttpResponse('else')


@csrf_exempt
def send(request):
    body_unicode = request.body.decode('utf-8')
    store = json.loads(body_unicode)
    name = str(store['name']) + str(store['age']) + str(store['amail'])
    progress = 0
    for t_name in store['user_topics']:
        top = store['user_topics'][t_name]
        progress += float(top['know_pr']) + float(top['repeat_pr']) + float(top['hair_pr'])
    progress = round(progress, 2)
    print('progress:', progress)
    print('name:', name)

    name_exist = Person.objects.filter(user_name=name)
    print('name_exist: ', name_exist)
    if len(name_exist) == 0:
        name_in_db = Person.objects.create(user_name=name, progress=progress, store=store)
        print('Create')
        print(progress, 'Send App version')
        return JsonResponse(store, safe=False)
    else:
        name_in_db = Person.objects.get(user_name=name)
        print(name_in_db.progress, name_in_db.progress <= progress, progress)

        if name_in_db.progress <= progress:
            print(progress, 'Send App version')
            name_in_db.progress = progress
            to_save = json.dumps(store)
            print('type(to_save)', type(to_save))
            name_in_db.store = to_save
            name_in_db.save()
            return JsonResponse(store, safe=False)
        else:
            print(name_in_db.progress, 'Send Serv version')
            return JsonResponse(json.loads(name_in_db.store), safe=False)
