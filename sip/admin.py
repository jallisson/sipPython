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
                'fields': ['numero_processo','ano_processo','notificado'],
            }),]

   class Meta:
             model = Processo


admin.site.register(Notificado)
admin.site.register(Processo, ProcessoAdmin)
admin.site.register(LoteFiscalizacao)
admin.site.register(MovimentoFiscalizacao)