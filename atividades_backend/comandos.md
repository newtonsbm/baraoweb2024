# Resumo dos principais comandos utilizados

- Instalando django
pip install django

- Outro comando para instalar o django
py -m pip install django

- Iniciando projeto django
django-admin startproject cafecompao

- Comando alternativo para iniciar projeto django
py -m django startproject cafecompao

- Comando para iniciar o servidor de desenvolvimento
python manage.py runserver

# Modularização
- Iniciar um app django chamado padarias
python manage.py startapp padarias

# ORM
- Criar migrations
python manage.py makemigrations 

- Aplicar migration
python manage.py migrate

# Reesetar o banco
- No SQLite basta deletar o arquivo db.sqlite3 e rodar as migrations novamente
- Se houver problemas em migrations basta deletar o banco, deletar todas as migrations e criar novamenteCestas

# Auth

- Criar super usuário
python manage.py createsuperuser
