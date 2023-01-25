from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.topic_name

class webpage(models.Model):
    topic_name=models.ForeignKey(topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    url=models.URLField()

    def __str__(self):
        return self.name

class accessrecords(models.Model):
    name=models.ForeignKey(webpage, on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    