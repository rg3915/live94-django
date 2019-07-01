# live94-django

Live de Python 94 - Django básico

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/live94-django.git
cd live94-django
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Criando um banco PostgreSql

```
sudo su - postgres
createdb live94
createuser -P dunossauro
pass: 94
psql live94
GRANT ALL PRIVILEGES ON DATABASE live94 TO dunossauro;
\q
exit
```

## Criando a pasta templates

```
mkdir -p myproject/core/templates/includes
touch myproject/core/templates/{base,index}.html
touch myproject/core/templates/includes/nav.html
```

https://gist.github.com/rg3915/0144a2408ec54c4e8008999631c64a30

## Criando um novo app

```
cd myproject
python ../manage.py startapp live
cd ..
tree
touch myproject/live/urls.py
mkdir -p myproject/live/templates/live
touch myproject/live/templates/live/live_{list,detail,form}.html
```


### Herança de templates

```html
{% extends "base.html" %}
```

## Forms e CreateView

```
touch myproject/live/forms.py
```

## Criando comandos personalizados

```
mkdir -p myproject/core/management/commands
touch myproject/core/management/__init__.py
touch myproject/core/management/commands/{__init__,import_lives}.py
```

O comando criado pode ser rodado com

```
python manage.py import_lives
```

## Filtrando campos calculados

```
res = [x.pk for x in Live.objects.all() if x.like_frequence < 0.2]
len(res)
```

## Links

[Tutorial Django 2.2](http://pythonclub.com.br/tutorial-django-2.html)

[Django doc oficial](https://www.djangoproject.com/)

[diagrama 1](https://raw.githubusercontent.com/rg3915/tutoriais/master/django-basic/img/diagrama.png)

[diagrama 2](https://raw.githubusercontent.com/rg3915/tutoriais/master/django-basic/img/mtv2.png)

[env_gen.py](https://gist.github.com/rg3915/22626de522f5c045bc63acdb8fe67b24)

[gist básico para criar os templates base.html e index.html](https://gist.github.com/rg3915/0144a2408ec54c4e8008999631c64a30)

[CBV](https://ccbv.co.uk)

[djangopackages](https://djangopackages.org/)

