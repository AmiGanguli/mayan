from django.contrib import admin
from api.models import ApiKey
from django.contrib.auth.models import User

class ApiKeyAdmin(admin.ModelAdmin):
    fields = ['name'] #, 'key']
    list_display = ('name', 'key', 'user')

admin.site.register(ApiKey, ApiKeyAdmin)


