from django.contrib import admin


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
admin.site.register(Leciono,LecionoAdmin)
