from django.contrib import admin

from .models import Questions, Choice
# Register your models here.

# admin.site.register(Questions)
# admin.site.register(Choise)

class ChoiceInline(admin.TabularInline):
    model =Choice

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]