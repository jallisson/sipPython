from django.urls import path
from django.conf.urls import include, url 
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView

from . import views
#from .views import VendaDetail
#from .views import RelatorioListView
#from .views import RelatorioDetail
#favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)


urlpatterns = [
    #path('', views.index, name='index'),
    #url(r'^venda/(?P<pk>\d+)/$', VendaDetail.as_view(), name='venda_detail'),
	#url(r'^lista/(?P<pk>\d+)/$', RelatorioListView.as_view(), name='venda_list'),
	#re_path(r'^favicon\.ico$', favicon_view),
	#url(r'^relatorio/(?P<pk>\d+)/$', RelatorioDetail.as_view(), name='venda_data_list'),
]
