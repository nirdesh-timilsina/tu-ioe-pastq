from django.contrib import admin

# Register your models here.
from .models import Subject, Chapter, Question, Appearance

admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Question)
admin.site.register(Appearance)