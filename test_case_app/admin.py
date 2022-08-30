from django.contrib import admin

from .models import Question, Choice


class Questions(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')
    list_display_links = ('id', 'question_text',)
    search_fields = ('question_text',)
    list_per_page = 20


admin.site.register(Question, Questions)


class Choices(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')
    list_filter = ('question',)
    list_display_links = ('id', 'choice_text',)
    search_fields = ('question__question_text', 'choice_text',)
    list_per_page = 20


admin.site.register(Choice, Choices)
