from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    sarlavha = models.CharField(max_length=150)
    batafsil = models.TextField()
    holat = models.CharField(max_length=100)
    vaqt = models.DateField()
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    def __str__(self):
        return self.sarlavha