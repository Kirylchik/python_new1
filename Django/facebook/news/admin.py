from django.contrib import admin

from .models import News
from .models import Posts

admin.site.register(News)
admin.site.register(Posts)
