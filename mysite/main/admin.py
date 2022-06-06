from django.contrib import admin
from .models import Food,Comment,User

admin.site.register(Food)
admin.site.register(Comment)
admin.site.register(User)