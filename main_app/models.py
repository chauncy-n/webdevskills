from django.db import models

# Create your models here.

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.skill
