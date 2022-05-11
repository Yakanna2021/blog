from django.urls import path
from .views import *

urlpatterns = [
    
    path('',SignupViews.as_view(),name='signup'),
]

