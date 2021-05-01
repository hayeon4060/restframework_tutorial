from django.urls import path
from .api import MeetingCreateApi, MeetingApi, MeetingUpdateApi, MeegingDeleteApi
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api',MeetingApi.as_view()),
    path('api/create',MeetingCreateApi.as_view()),
    path('api/<int:pk>', MeetingUpdateApi.as_view()),
    path('api/<int:pk>/delete', MeegingDeleteApi.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)