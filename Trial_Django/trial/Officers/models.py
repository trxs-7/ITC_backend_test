from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class CommitteeOfficer(models.Model):
    id = models.AutoField(
        auto_created = True,
        primary_key = True,
        serialize = False,
        verbose_name ='ID'
        )
    name = models.CharField(
        max_length = 50, 
        blank = False
        )
    year = models.IntegerField(
        validators = [
            MinValueValidator(1),
            MaxValueValidator(4)
        ],
        blank = False
        )
    hobby = models.CharField(
        max_length = 50,
        blank = True
        )
    
    def __str__(self):
        return f'<ID {self.id}: {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'hobby': self.hobby
        }