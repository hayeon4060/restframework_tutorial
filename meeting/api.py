from rest_framework import generics
from rest_framework.response import Response
from .serializer import MeetingSerializer
from .models import Meeting
class MeetingCreateApi(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class MeetingApi(generics.ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class MeetingUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class MeegingDeleteApi(generics.DestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer



