from django.db import models

# Create your models here.
class meeting(models.Model):
    id = models.TextField(unique=True)
    title = models.TextField()
    topic = models.TextField()
    writer = models.TextField()
    parties = models.TextField()
    date = models.DateTimeField(auto_now=True)
    # file = models.FileField(upload_to = u'talks/', max_length=200)