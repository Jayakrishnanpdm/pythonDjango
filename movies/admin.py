from django.contrib import admin
from . models import movie_info,Directors

# Register your models here.
admin.site.register(movie_info)
admin.site.register(Directors)