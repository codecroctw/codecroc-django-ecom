from django.contrib import admin
from .models import UserProfile, ContactForm

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ContactForm)
