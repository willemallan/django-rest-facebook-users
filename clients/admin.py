# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('facebook_id', 'name', 'username', 'gender')
    search_fields = ('facebook_id', 'name', 'username', 'gender')
    save_on_top = True
    

admin.site.register(Client, ClientAdmin)