from django.contrib import admin

from .models import Notice_Question, Free_Question, Info_Question

class Notice_QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Notice_Question, Notice_QuestionAdmin)

class Free_QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Free_Question, Free_QuestionAdmin)

class Info_QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Info_Question, Info_QuestionAdmin)