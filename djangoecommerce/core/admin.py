from django.contrib import admin

from djangoecommerce.core.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email', 'message']


admin.site.register(Contact, ContactAdmin)
