from django.contrib import admin

from .models import *
from django.contrib.auth.models import User

admin.site.register(Ryans)
admin.site.register(Search)
admin.site.register(Notification)
admin.site.register(SearchHit)
admin.site.register(UserActivity)


