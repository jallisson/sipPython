from django.contrib import admin
from .models import Notificado
from .models import Processo
from .models import LoteFiscalizacao
from .models import MovimentoFiscalizacao

#from .models import Processo



#class ProdutoInline(admin.TabularInline):
#   model = Produto

class ProcessoAdmin(admin.ModelAdmin):

   list_display = ('processo','ano_processo','notificado')
   list_per_page = 50
   search_fields = ('processo',)
   #ordering = ('nome',)

   fieldsets = [
            ('Dados Principais', {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': ['numero_processo','ano_processo','notificado','usuario'],
            }),]

   class Meta:
             model = Processo

   def save_model(self, request, obj, form, change):
	    if getattr(obj, 'usuario', None) is None:
		    obj.usuario = request.user
	    obj.save()

class MovimentoFiscalizacaoAdmin(admin.ModelAdmin):

   list_display = ('processo','lote','tipo', 'observacao')
   list_per_page = 50
   search_fields = ('processo',)
   #ordering = ('nome',)

   fieldsets = [
            ('Dados Principais', {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': ['processo','tipo','lote','observacao','usuario'],
            }),]

   class Meta:
             model = MovimentoFiscalizacao

   def save_model(self, request, obj, form, change):
	    if getattr(obj, 'usuario', None) is None:
		    obj.usuario = request.user
	    obj.save()


admin.site.register(Notificado)
admin.site.register(Processo, ProcessoAdmin)
admin.site.register(LoteFiscalizacao)
admin.site.register(MovimentoFiscalizacao, MovimentoFiscalizacaoAdmin)