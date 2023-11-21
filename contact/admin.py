from django.contrib import admin

from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'AKA', 'name', 'phone',
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'AKA', 'name',
    list_per_page = 10
    list_max_show_all = 25
    list_editable = 'AKA', 'name',
    list_display_links = 'id', 'phone',
