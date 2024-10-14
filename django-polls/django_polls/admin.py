from django.contrib import admin
from .models import *

class ChoiceInline(admin.TabularInline):
    model=Choice
    extras=3

class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text','pub_date','was_published_recently')
    # fields=['pub_date','question_text']
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date informations',{'fields':['pub_date'],'classes':'collapse'})]
    inlines=[ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)