from django.contrib import admin
from .models import Notificado
#from .models import Processo



#class ProdutoInline(admin.TabularInline):
#   model = Produto


admin.site.register(Notificado)
#admin.site.register(Processo, ProcessoAdmin)