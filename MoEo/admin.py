from django.contrib import admin

from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInLine]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_per_page = 20
	list_filter = ['pub_date']
	search_fields = ['question_text']
#################################################################
# aldoni la modelojn
from .models import Leciono, Teksto, Frazo, Vorto, Noto

class TekstoInLine(admin.TabularInline):
	model = Teksto
	extra = 0

class FrazoInLine(admin.TabularInline):
	model = Frazo
	extra = 0

class VortoInLine(admin.TabularInline):
	model = Vorto
	extra = 5

class NotoInLine(admin.TabularInline):
	model = Noto
	extra = 0

class LecionoAdmin(admin.ModelAdmin):
	fields = ['leciono']
	inlines = [TekstoInLine,FrazoInLine,VortoInLine]
	list_display = ['leciono']
	list_filter = ['leciono']

# registrigi la modelojn
admin.site.register(Question,QuestionAdmin)
admin.site.register(Leciono,LecionoAdmin)
