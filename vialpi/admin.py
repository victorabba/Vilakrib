from django.contrib import admin
from .models import User, ContactUs
from django.contrib.auth.admin import UserAdmin



class UserAdmin(UserAdmin):
    list_display=('Register_as','first_name','last_name','email','username','phone_number')
    search_fields=('email','username')
    readonly_fields=('date_joined','last_login')

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(User, UserAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display=('full_name','email','phone_number','your_message')

admin.site.register(ContactUs, ContactUsAdmin)

