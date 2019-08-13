from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


class VotersAdmin(admin.ModelAdmin):
    list_display = ('name', 'aadhar','sex')
    search_fields = ('aadhar', 'name', 'sex')


class PartiesAdmin(admin.ModelAdmin):
    list_display = ('pname','logo','nominatior','description')
    search_fields = ('pname','nominatior')


admin.site.register(Voters, VotersAdmin)
admin.site.register(Parties,PartiesAdmin)
admin.site.register(CustomUser, CustomUserAdmin)