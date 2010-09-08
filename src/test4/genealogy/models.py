from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    
    first_name = models.CharField(max_length=31)
    second_name = models.CharField(max_length=31, blank=True)
    third_name = models.CharField(max_length=31, blank=True)
    surname_at_birth = models.CharField(max_length=31)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    mother = models.ForeignKey("Person", related_name="mothered", blank=True, null=True)
    father = models.ForeignKey("Person", related_name="fathered", blank=True, null=True)
    
    def __unicode__(self):
        return self.first_name + " " + self.surname_at_birth # + " (" + str(self.date_of_birth) + ")"
    
    class Meta:
        verbose_name_plural = "people"
    
class Marriage(models.Model):
    husband = models.ForeignKey(Person, related_name="husband_of")
    wife = models.ForeignKey(Person, related_name="wife_of")
    date_of_marriage = models.DateField(blank=True)
    
    def __unicode__(self):
        return "marriage of " + self.husband.first_name + " " + self.husband.surname_at_birth + " to " + self.wife.first_name + " " + self.wife.surname_at_birth
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, blank=True, null=True)
    person = models.ForeignKey(Person)
