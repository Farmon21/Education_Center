from django.contrib import admin
from .models import Application, Course, Teacher

# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Application)
