from django.contrib import admin
from .models import Curso, Modulo, Licao
# Register your models here.

class LicaoInline(admin.StackedInline):
    model = Licao
    extra = 1
    
class ModuloInline(admin.StackedInline):
    model = Modulo
    extra =1
    inlines = [LicaoInline]
    
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instrutor', 'criado_em', 'atualizado_em')
    inlines = [ModuloInline]
    
@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'order')
    inlines = [LicaoInline]
    
@admin.register(Licao)
class LicaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'modulo', 'order')
    