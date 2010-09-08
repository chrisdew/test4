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
 
admin.site.register(User, UserProfileAdmin)

admin.site.register(models.Person)
admin.site.register(models.Marriage)
