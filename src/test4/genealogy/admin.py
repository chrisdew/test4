import test4.genealogy.models as models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from test4.genealogy.models import UserProfile
 
admin.site.unregister(User)
 
class UserProfileInline(admin.StackedInline):
    model = UserProfile
 
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]
 
class ManManInline(admin.StackedInline): 
    fk_name = 'father'
    extra=1
    model = models.Man
    
class WomanManInline(admin.StackedInline): 
    fk_name = 'father'
    extra=1
    model = models.Woman
 
class BaptismInline(admin.StackedInline):
    extra=1
    model = models.Baptism

class OccupationInline(admin.StackedInline):
    extra=1
    model = models.Occupation

class CensusInline(admin.StackedInline):
    extra=1
    model = models.Census

class MarriageManInline(admin.StackedInline):
    fk_name = 'husband'
    extra=1
    model = models.Marriage 

class MarriageWomanInline(admin.StackedInline):
    fk_name = 'wife'
    extra=1
    model = models.Marriage 
 
class ManAdmin(admin.ModelAdmin):
    inlines = [BaptismInline, MarriageManInline, ManManInline, WomanManInline, OccupationInline, CensusInline] 

class WomanAdmin(admin.ModelAdmin):
    inlines = [BaptismInline, MarriageWomanInline, OccupationInline, CensusInline] 

 
admin.site.register(User, UserProfileAdmin)

admin.site.register(models.Person) #, PersonAdmin)
admin.site.register(models.Man, ManAdmin)
admin.site.register(models.Woman, WomanAdmin)
admin.site.register(models.Marriage)
admin.site.register(models.Baptism)
admin.site.register(models.Occupation)
admin.site.register(models.Census)
