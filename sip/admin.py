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
                'fields': ['numero_processo','ano_processo','notificado'],
            }),]

   class Meta:
             model = Processo

   def save_model(self, request, obj, form, change):
            if getattr(obj, 'usuario', None) is None:
                    obj.usuario = request.user
            #if getattr(obj, 'agencia', None) is None:
            #        obj.agencia = request.user.groups.first()
            obj.save()

class MovimentoFiscalizacaoAdmin(admin.ModelAdmin):

   list_display = ('processo','notificado','data','lote','tipo','observacao','usuario')
   list_per_page = 50
   search_fields = ('processo__processo', 'processo__notificado__nome')
   #ordering = ('nome',)

   fieldsets = [
            ('Dados Principais', {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': ['processo','tipo','lote','observacao'],
            }),]

   class Meta:
             model = MovimentoFiscalizacao

   def notificado(self, obj):
          return obj.processo.notificado.nome
         #get_name.admin_order_field  = 'name'  #Allows column order sorting
          notificado.short_description = 'Notificado'  #Renames column head

   def save_model(self, request, obj, form, change):
            if getattr(obj, 'usuario', None) is None:
                    obj.usuario = request.user
            #if getattr(obj, 'agencia', None) is None:
            #        obj.agencia = request.user.groups.first()
            obj.save()

class NotificadoAdmin(admin.ModelAdmin):

   list_display = ('nome','cnpj','cpf')
   list_per_page = 50
   search_fields = ('nome',)
   #ordering = ('nome',)

   class Meta:
             model = Notificado


admin.site.register(Notificado, NotificadoAdmin)
admin.site.register(Processo, ProcessoAdmin)
admin.site.register(LoteFiscalizacao)
admin.site.register(MovimentoFiscalizacao, MovimentoFiscalizacaoAdmin)