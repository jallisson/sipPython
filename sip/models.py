# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from datetime import datetime
import sys
import time
from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.utils.html import mark_safe
from django.db.models import F, FloatField, Sum
from decimal import Decimal
from django import forms
from django.core.exceptions import (
    NON_FIELD_ERRORS, FieldError, ImproperlyConfigured, ValidationError,
)

class Notificado(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    cpf = models.CharField(max_length=18, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=50, choices = STATE_CHOICES)
    #cep = models.CharField(max_length=8, null=True)
    telefone = models.CharField(max_length=14)
    #email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        self.endereco = self.endereco.upper()
        self.bairro = self.bairro.upper()
        self.cidade = self.cidade.upper()
        super(Notificado, self).save(force_insert, force_update)

ANOS = (
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
    )

class Processo(models.Model):
    numero_processo = models.CharField(max_length=4)
    ano_processo = models.CharField(max_length=4, choices = ANOS, default='2020', null=True, blank=True)
    processo = models.CharField(max_length=20, unique=True)
    notificado = models.ForeignKey(Notificado, on_delete=models.CASCADE)
    #pdf = models.FileField(default=None)
    usuario = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.processo)

    class Meta:
        unique_together = (("numero_processo", "ano_processo"),)

    def save(self, *args, **kwargs):
        self.processo = "%s %s/%s" % ("FI",str(self.numero_processo.zfill(4)) , self.ano_processo)
        super(Processo, self).save()


class LoteFiscalizacao(models.Model):
    descricao = models.CharField(max_length=100, default=None, unique=True)

    def __str__(self):
        return str(self.descricao)

    def save(self, force_insert=False, force_update=False):
        self.descricao = self.descricao.upper()
        super(LoteFiscalizacao, self).save(force_insert, force_update)



TIPO = (
        ('ENTRADA', 'ENTRADA'),
        ('SAÍDA', 'SAÍDA')
    )

class MovimentoFiscalizacao(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)
    lote = models.ForeignKey(LoteFiscalizacao, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True, verbose_name=u'Data',)
    tipo = models.CharField(max_length=20, choices = TIPO, default='ENTRADA', null=True, blank=True)
    observacao = models.CharField(max_length=40,  null=True, blank=True)
    controle = models.CharField(max_length=40, default=None, unique=True)#, error_messages={'UniqueValidator':"This email has already been registered."})
    usuario = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
   
    def __str__(self):
        return str(self.processo)

    def save(self, *args, **kwargs):
        self.controle = "%s-%s" % (str(self.processo) , str(self.tipo))
        super(MovimentoFiscalizacao, self).save()

TIPOS = (
        ('LISTA LOTE FISCALIZAÇÃO', 'LISTA LOTE FISCALIZAÇÃO'),
    )

class Relatorio(models.Model):
    tipo = models.CharField(max_length=30, choices = TIPOS, default='LISTA LOTE FISCALIZAÇÃO')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    lote = models.ForeignKey(LoteFiscalizacao, on_delete=models.CASCADE, null=True, blank=True)

    def imprimir(self):
        return mark_safe("<a target='_blank' href='%s'>Imprimir</a>" % self.get_absolute_url())
    imprimir.allow_tags = True

    def get_absolute_url(self):
        return reverse('mfiscalizacao_data_list', args=[self.pk, ])

    def __str__(self):
        return str(self.lote)

POTENCIAL = (
        ('ALTA', 'ALTA'),
        ('MÉDIA', 'MÉDIA'),
        ('BAIXA', 'BAIXA')
    )

class Atividade(models.Model):
    nome = models.CharField(max_length=100, default=None, unique=True)
    potencial_poluidor = models.CharField(max_length=30, choices = POTENCIAL, default='ALTA')

    def __str__(self):
        return str(self.nome)

    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        super(Atividade, self).save(force_insert, force_update)