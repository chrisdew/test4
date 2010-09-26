from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    #GENDER_CHOICES = (
    #    (u'M', u'Male'),
    #    (u'F', u'Female'),
    #)
    
    first_name = models.CharField(max_length=31)
    second_name = models.CharField(max_length=31, blank=True)
    third_name = models.CharField(max_length=31, blank=True)
    surname_at_birth = models.CharField(max_length=31, blank=True)
    #gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True)
    date_of_death = models.DateField(blank=True, null=True)

    mother = models.ForeignKey("Woman", blank=True, null=True)
    father = models.ForeignKey("Man", blank=True, null=True)
    father_occupation = models.CharField(max_length=31, blank=True)
    
    notes = models.TextField(blank=True)
    
    
    def __unicode__(self):
        return self.first_name + " " + self.surname_at_birth # + " (" + str(self.date_of_birth) + ")"
    
    class Meta:
        verbose_name_plural = "people"
    
class Man(Person):
    def __unicode__(self):
        marriages = Marriage.objects.filter(husband=self)
        if len(marriages) > 0:
            return self.first_name + " " + self.surname_at_birth + ", husband of " + marriages[0].wife.first_name + " " + marriages[0].wife.surname_at_birth   
        return self.first_name + " " + self.surname_at_birth # + " (" + str(self.date_of_birth) + ")"


    class Meta:
        verbose_name_plural = "men"

class Woman(Person):
    def __unicode__(self):
        marriages = Marriage.objects.filter(wife=self)
        if len(marriages) > 0:
            return self.first_name + " " + self.surname_at_birth + ", wife of " + marriages[0].husband.first_name + " " + marriages[0].husband.surname_at_birth   
        return self.first_name + " " + self.surname_at_birth # + " (" + str(self.date_of_birth) + ")"

    class Meta:
        verbose_name_plural = "women"
        
    
class Baptism(models.Model):
    person = models.ForeignKey(Person)
    date_of_baptism = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    
class Occupation(models.Model):
    person = models.ForeignKey(Person)
    year = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=31, blank=True)
    address = models.CharField(max_length=255, blank=True)
    
class Census(models.Model):
    person = models.ForeignKey(Person)
    year = models.IntegerField(null=True, blank=True)
    subdistrict = models.CharField(max_length=255, blank=True)
    ed = models.CharField(max_length=4, blank=True)
    head_of_household = models.CharField(max_length=255, blank=True)
    birthplace = models.CharField(max_length=255, blank=True)
    living_with = models.CharField(max_length=255, blank=True)
    
    
class Marriage(models.Model):
    husband = models.ForeignKey(Man, related_name="husband_of")
    wife = models.ForeignKey(Woman, related_name="wife_of")
    date_of_marriage = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)    
    witness_names = models.CharField(max_length=255, blank=True)    
    
    def __unicode__(self):
        return "marriage of " + self.husband.first_name + " " + self.husband.surname_at_birth + " to " + self.wife.first_name + " " + self.wife.surname_at_birth
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, blank=True, null=True)
    person = models.ForeignKey(Person)
