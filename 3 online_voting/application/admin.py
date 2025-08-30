from django.contrib import admin

# Register your models here.
from .models import candidate,voter,cast_vote

admin.site.register(candidate)
admin.site.register(voter)
admin.site.register(cast_vote)