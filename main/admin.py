from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class CitizenInline(admin.StackedInline):
    model = Citizen
    can_delete = False
    verbose_name_plural = 'citizens'

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (CitizenInline,)


admin.site.register(Petition)
admin.site.register(Comment)
admin.site.register(Citizen)
