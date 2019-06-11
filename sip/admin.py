from django.contrib import admin
from .models import Notificado
from .models import Processo
from .models import LoteFiscalizacao
from .models import MovimentoFiscalizacao
from .models import Relatorio
from django import forms
from django.forms.models import BaseInlineFormSet
#from .models import Processo




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

   def pdf(self, obj):
          return obj.processo.pdf
         #get_name.admin_order_field  = 'name'  #Allows column order sorting
          pdf.short_description = 'Pdf'  #Renames column head

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


class RelatorioForm(forms.ModelForm):
    TIPOS = (
        ('LISTA LOTE FISCALIZAÇÃO', 'LISTA LOTE FISCALIZAÇÃO'),
    )
    
    tipo = forms.CharField(widget=forms.RadioSelect(attrs={'class': 'inline'}, choices=TIPOS), initial='LISTA LOTE FISCALIZAÇÃO')
    
    class Meta:
        model = Relatorio
        fields = ['tipo',]

    

class RelatorioAdmin(admin.ModelAdmin):

   list_display = ('id', 'tipo', 'lote', 'usuario', 'imprimir',)
   list_per_page = 50
   form = RelatorioForm

   class Meta:
             model = Relatorio

   fieldsets = [
            ('Dados Principais', {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': ['tipo', 'lote'],
            }),]

   def save_model(self, request, obj, form, change):
            if getattr(obj, 'usuario', None) is None:
                    obj.usuario = request.user
            #if getattr(obj, 'agencia', None) is None:
            #        obj.agencia = request.user.groups.first()
            obj.save()

class LoteFiscalizacaoAdmin(admin.ModelAdmin):

   list_display = ('descricao',)
   list_per_page = 50
   search_fields = ('descricao',)
   #ordering = ('nome',)

   class Meta:
             model = LoteFiscalizacao




admin.site.register(Relatorio, RelatorioAdmin)
admin.site.register(Notificado, NotificadoAdmin)
admin.site.register(Processo, ProcessoAdmin)
admin.site.register(LoteFiscalizacao, LoteFiscalizacaoAdmin)
admin.site.register(MovimentoFiscalizacao, MovimentoFiscalizacaoAdmin)