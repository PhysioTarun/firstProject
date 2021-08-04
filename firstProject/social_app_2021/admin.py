from django.contrib import admin
from .models import UserProfile, Group, Event, Feed

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Feed)
