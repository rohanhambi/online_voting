from django.contrib import admin
from vote.models import Voter,Party
# Register your models here.
admin.site.register(Voter)
admin.site.register(Party)