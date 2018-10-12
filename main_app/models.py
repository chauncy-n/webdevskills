from django.db import models
from django.contrib.auth.models import User

# Create your models here.

LEVELS = (
    (1, 'Fundamental awareness'),
    (2, 'Novice'),
    (3, 'Intermediate'),
    (4, 'Advanced'),
    (5, 'Expert'),
)

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    skill_level = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.skill

class SkillLevel(models.Model):
    levels = models.IntegerField(
        choices=LEVELS,
        default=LEVELS[0][0] 
    )
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    


