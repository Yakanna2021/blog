from django import views
from django.urls import path
from .views import *
from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('post/<int:pk>/',DetailView.as_view(),name='index'),
    path('new/',CreateView.as_view(),name='create'),
    path('post/<int:pk>/edit',UpdateView.as_view(),name='update'),
    path('post/<int:pk>/Delete',DeleteView.as_view(),name='Delete'),
   
]

#urlpatterns += staticfiles_urlpatterns()

