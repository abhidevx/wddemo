# imports
from django.contrib import admin
from home.models import Customer, Profile


# Register models at admin .
admin.site.register(Customer)
admin.site.register(Profile)
