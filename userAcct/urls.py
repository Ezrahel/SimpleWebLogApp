from django.urls import path, include
from . import views
app_name = 'userAcct'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]