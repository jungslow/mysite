from django.contrib import admin
from .models import Question
from .models import Answer
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['author']
admin.site.register(Answer, AnswerAdmin)