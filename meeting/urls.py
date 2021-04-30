from django.urls import path
from .api import MeetingCreateApi
# from .api import MeetingApi
urlpatterns = [
    # path('api',MeetingApi.as_view()),
    path('api/create',MeetingCreateApi.as_view()),
]