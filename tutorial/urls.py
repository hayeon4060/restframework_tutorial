from django.urls import include, path
from rest_framework import routers
from quickstart import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', include('snippets.urls')),
    path('', include('meeting.urls')),
   
]



# from django.conf.urls import url
# from django.urls import path, include
# from django.contrib import admin
# from meeting.api import MeetingApi
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
    
   
#     path('meeting/', include('meeting.urls')),
# ]