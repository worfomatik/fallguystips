from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    owner = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE, null=True)  #added
    # created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())

    def _str_(self):
        return self.title