from django.contrib import admin

# Register your models here.
from .models import Photo
from .models import Message
admin.site.register(Photo)
admin.site.register(Message)
