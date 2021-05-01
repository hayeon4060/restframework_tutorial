from django.db import models

# Create your models here.
class Meeting(models.Model):
    # id = models.AutoField(primary_key=True) 자동으로 추가됨
    title = models.TextField()
    topic = models.TextField()
    writer = models.TextField()
    parties = models.TextField()
    meeting_date = models.DateTimeField()
    date = models.DateTimeField(auto_now=True) #자동추가
    file = models.FileField(upload_to = u'audio/')