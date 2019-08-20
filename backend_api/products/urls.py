
from django.urls import path
from .views import *

urlpatterns = [
    path('',CustomAuthToken.as_view() )
]
