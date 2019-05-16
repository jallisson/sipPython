from django.contrib import admin
from .models import Notificado
from .models import Processo
from .models import LoteFiscalizacao
from .models import MovimentoFiscalizacao

#from .models import Processo



#class ProdutoInline(admin.TabularInline):
#   model = Produto

class ProcessoAdmin(admin.ModelAdmin):

   list_display = ('processo','ano_processo','notificado','usuario')
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
<<<<<<< HEAD
            if getattr(obj, 'usuario', None) is None:
                    obj.usuario = request.user
            #if getattr(obj, 'agencia', None) is None:
            #        obj.agencia = request.user.groups.first()
            obj.save()
=======
	    if getattr(obj, 'usuario', None) is None:
		    obj.usuario = request.user
	    obj.save()
>>>>>>> afda26e175b24db5a84c57d1fe27ffeff7613acf

class MovimentoFiscalizacaoAdmin(admin.ModelAdmin):

   list_display = ('processo','data','lote','tipo','observacao','usuario')
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
<<<<<<< HEAD
            if getattr(obj, 'usuario', None) is None:
                    obj.usuario = request.user
            #if getattr(obj, 'agencia', None) is None:
            #        obj.agencia = request.user.groups.first()
            obj.save()
=======
	    if getattr(obj, 'usuario', None) is None:
		    obj.usuario = request.user
	    obj.save()
>>>>>>> afda26e175b24db5a84c57d1fe27ffeff7613acf


admin.site.register(Notificado)
admin.site.register(Processo, ProcessoAdmin)
admin.site.register(LoteFiscalizacao)
admin.site.register(MovimentoFiscalizacao, MovimentoFiscalizacaoAdmin)