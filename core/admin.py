from django.contrib import admin
from .models import Course, News, Feedback, Teacher

admin.site.register(Course)
admin.site.register(News)
admin.site.register(Feedback)
admin.site.register(Teacher)
