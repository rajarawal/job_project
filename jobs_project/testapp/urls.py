from django.urls import path
from testapp.views import *


urlpatterns =[
    path('hydjobs/',hydJobsView),
    path('blorejobs/',bloreJobsView),
    path('punejobs/',puneJobsView),
    path('chennaijobs/',chennaiJobsView),
]
