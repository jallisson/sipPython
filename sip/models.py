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


class Notificado(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    cpf = models.CharField(max_length=18, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=50, choices = STATE_CHOICES)
    cep = models.CharField(max_length=8, null=True)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        self.endereco = self.endereco.upper()
        self.bairro = self.bairro.upper()
        self.cidade = self.cidade.upper()
        super(Notificado, self).save(force_insert, force_update)
