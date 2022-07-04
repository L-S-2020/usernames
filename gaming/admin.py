from django.contrib import admin
from .models import usernames

# Register your models here.

# It adds the usernames model to the admin page.
admin.site.register(usernames)
