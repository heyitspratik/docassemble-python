from django.contrib import admin
from .models import QuestionData


@admin.register(QuestionData)
class QuestionDataAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('question','currency','value')
    list_display = ('id','question','currency','value')