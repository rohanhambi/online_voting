from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from users import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('parties/', views.parties_new, name='parties_new'),
    path('homepage/', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('parties/', TemplateView.as_view(template_name='parties.html'), name='parties'),
    path('votenow/',TemplateView.as_view(template_name='votenow.html'), name = 'votenow'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
