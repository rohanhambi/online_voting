from django.contrib import admin
from .models import Voters, User, Parties
from django.contrib.auth.admin import UserAdmin
# Register your models here.
'''
username: amulya
pswd: a'''


class VotersAdmin(admin.ModelAdmin):
    list_display = ('name', 'aadhar', 'votingstatus')
    search_fields = ('aadhar', 'name', 'votingstatus', 'sex')


class PartiesAdmin(admin.ModelAdmin):
    list_display = ('pname','logo','nominatior')
    search_fields = ('pname','nominatior')


admin.site.register(User, UserAdmin)
admin.site.register(Voters, VotersAdmin)
admin.site.register(Parties,PartiesAdmin)
