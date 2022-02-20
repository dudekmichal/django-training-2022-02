from django.contrib import admin

# Register your models here.
from .models import Person, Guard, Suit

admin.site.register(Person)
admin.site.register(Guard)
admin.site.register(Suit)
