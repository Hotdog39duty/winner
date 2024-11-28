from django.db import models

# Create your models here.


class Post(models.Model):
    # Default behaviour
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Khanya")
    date = models.DateTimeField()

    def __str__(self):
        return self.title
