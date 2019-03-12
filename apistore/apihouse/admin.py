from django.contrib import admin
from .models import Author, Blog, ContactUs, Country

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Country)
admin.site.register(ContactUs)
