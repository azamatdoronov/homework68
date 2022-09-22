from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Profile


# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)
