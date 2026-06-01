from django.contrib import admin
from .models import Subject, Chapter, Question, Appearance

class AppearanceInline(admin.TabularInline):
    model = Appearance
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    fields = ['text', 'marks', 'frequency']
    extra = 0
    show_change_link = True

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'semester']
    list_filter = ['semester']
    search_fields = ['code', 'name']
    ordering = ['semester', 'code']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'order', 'title']
    list_filter = ['subject']
    search_fields = ['title']
    ordering = ['subject', 'order']
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['short_text', 'chapter', 'marks', 'frequency']
    list_filter = ['chapter__subject']
    search_fields = ['text']
    inlines = [AppearanceInline]

    def short_text(self, obj):
        return obj.text[:80]
    short_text.short_description = 'Question'

@admin.register(Appearance)
class AppearanceAdmin(admin.ModelAdmin):
    list_display = ['question', 'year', 'session', 'exam_type']
    list_filter = ['exam_type', 'year']