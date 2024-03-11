from django.db import models


# Create your models here.

class ToDoTask(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
