from django.contrib import admin
from .models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):

    list_display = (
        'visitor_name',
        'phone',
        'company',
        'purpose',
        'person_to_meet',
        'vehicle_number',
        'check_in',
        'check_out',
        'status',
    )

    list_filter = ('status', 'check_in')

    search_fields = (
        'visitor_name',
        'phone',
        'vehicle_number',
        'company',
    )