from django.urls import path
from .api import MeetingCreateApi, MeetingApi, MeetingUpdateApi, MeegingDeleteApi

urlpatterns = [
    path('api',MeetingApi.as_view()),
    path('api/create',MeetingCreateApi.as_view()),
    path('api/<int:pk>', MeetingUpdateApi.as_view()),
    path('api/<int:pk>/delete', MeegingDeleteApi.as_view()),
]