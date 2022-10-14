from atexit import register
from django.contrib import admin

from enigma_tempo.models import Card

# Register your models here.
admin.site.register(Card)
