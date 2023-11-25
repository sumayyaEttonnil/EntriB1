

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, BookedSeat


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'phone_number'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone_number', )
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone_number',)
        })
    )

from .models import Bus, Stop, BoardingStop, DestinationStop

class BoardingStopInline(admin.TabularInline):
    model = BoardingStop

class DestinationStopInline(admin.TabularInline):
    model = DestinationStop

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    inlines = [
        BoardingStopInline,
        DestinationStopInline,
    ]

admin.site.register(Stop)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(BookedSeat)



