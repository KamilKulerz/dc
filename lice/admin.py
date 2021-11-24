from django.contrib import admin
from lice.models import AppUser
from django.contrib.auth.admin import UserAdmin


class AppProfileAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Active', 'FullAccess', 'LicenseSignAccess')


admin.site.register(AppUser, AppProfileAdmin)
