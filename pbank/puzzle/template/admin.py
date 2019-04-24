from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Categories)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
