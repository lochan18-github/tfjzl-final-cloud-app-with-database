from django.contrib import admin
from .models import Question, Choice, Submission, Lesson, Course, Instructor


# Inline for Choices
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Inline for Questions
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text',)


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course)
admin.site.register(Instructor)
