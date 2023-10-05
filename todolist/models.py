from django.db import models


# Create your models here.
class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
