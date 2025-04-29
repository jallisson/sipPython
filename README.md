# Sip [![Build Status](https://travis-ci.org/thiagopena/djangoSIGE.svg?branch=master)](https://travis-ci.org/thiagopena/djangoSIGE)

Sistema para controle de processos

Projeto independente open-source desenvolvido em Python 3 no Windows, testado no GNU/Linux e Windows.


## Dependências

- [Python](https://www.python.org/downloads/) - Versão 3.5+
- [django](http://www.djangoproject.com) == 3.1.7
- [apache2](https://www.apache.org/) (Opcional)
- [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/) (Opcional)

## Instalação:

0. Instalar as bibliotecas/pacotes (no Linux):

1. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Sincronize a base de dados:

```bash
python manage.py migrate
```

5. Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):

```bash
python manage.py runserver
```

## Créditos

- [jallisson](https://github.com/jallisson)


## Ajuda

Como este é um projeto em desenvolvimento, qualquer feedback será bem-vindo.
