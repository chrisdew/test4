from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    
    first_name = models.CharField(max_length=31)
    second_name = models.CharField(max_length=31)
    third_name = models.CharField(max_length=31)
    surname_at_birth = models.CharField(max_length=31)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    mother = models.ForeignKey("Person", related_name="mothered")
    father = models.ForeignKey("Person", related_name="fathered")
    
class Marriage(models.Model):
    husband = models.ForeignKey(Person, related_name="husband_of")
    wife = models.ForeignKey(Person, related_name="wife_of")
    date_of_marriage = models.DateField()
    date_of_divorce = models.DateField()
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    person = models.ForeignKey(Person)
