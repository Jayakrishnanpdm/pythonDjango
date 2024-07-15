from django.contrib import admin
from . models import movie_info,Directors,Actors,Censor_info

# Register your models here.
admin.site.register(movie_info)
admin.site.register(Directors)
admin.site.register(Actors)
admin.site.register(Censor_info)