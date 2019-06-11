# -- coding: utf-8 --
#from _future_ import unicode_literals

from django.shortcuts import render

from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.auth.models import User, Group
from .models import LoteFiscalizacao
from .models import MovimentoFiscalizacao
from .models import Relatorio
from django.http import HttpResponse

class RelatorioDetail(DetailView):
    model = Relatorio
    

    def get_template_names(self):
        pk = self.kwargs['pk']
        obj = Relatorio.objects.get(pk=pk)
        return 'sip/mfiscalizacao_data_list.html'
    
    def get_context_data(self, **kwargs):
        #inicio = self.object.data_inicial
        #fim = self.object.data_final
        lote = self.object.lote
        #usuario = self.object.usuario
        #usuario = self.object.usuario
        #eturn self.model.filter(user=request.user)
    	
        return dict(
            super(RelatorioDetail, self).get_context_data(**kwargs),
            movimentofiscalizacao_list = MovimentoFiscalizacao.objects.filter(lote=lote),
            #venda_list_geral = Venda.objects.filter(data_venda__range=[inicio, fim]),
            #recebimento_list = Recebimento.objects.filter(data_recebimento__range=[inicio, fim]).filter(usuario=self.request.user),
            #recebimento_list = Recebimento.objects.filter(data_recebimento__range=[inicio, fim]).filter(usuario=self.request.user), filtro buscando usuario logado

        )