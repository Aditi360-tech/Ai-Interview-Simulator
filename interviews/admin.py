from django.contrib import admin

from .models import *
admin.site.register(InterviewSession)
admin.site.register(Question)
admin.site.register(Answer)
