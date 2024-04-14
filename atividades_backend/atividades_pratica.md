# Programação Web - Atividades Práticas

Prof. Newton Miyoshi - newton.miyoshi@baraodemaua.br

## Atividade 1 - Iniciando Projeto Django

1. Criar um projeto Django chamado `cafecompao`
2. Criar aplicação chamada `padarias`

### Resumo dos Conceitos Importantes
Nesta atividade vamos criar de uma aplicação web fullstack. Diversos frameworks fullstack utilizam o padrão [MVC (Model-View-Controller)](https://developer.mozilla.org/en-US/docs/Glossary/MVC) que no caso particular do django utiliza uma variação desse modelo chamado [MVT (Model-View-Template)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction). 

Todo framework de desenvolvimento web terá uma estrutura de pastas e arquivos que são necessários para o funcionamento do projeto. No caso do Django, temos a pasta do projeto principal que contém as configurações gerais (settings.py). Além disso todo framework também terá ferramentas de linha de comando (cli tools) que facilitam a criação de novos componentes do projeto além de outros utilitários. No caso do django essas ferramentas são o django-admin e o manage.py.

Por fim, outro conceito importante é da modularização e reuso de código. Todo framework agrupará seu código em módulos que podem ser reutilizados em diferentes projetos. No caso do Django, esses módulos são chamados de aplicações e são criados a partir do comando `startapp` do manage.py.

### Projeto Django

- Instalar Python: https://www.python.org/downloads/
- Instalar Django: `pip install django` ou `py -m pip install django`
- Criar projeto Django: `django-admin startproject cafecompao` ou `py -m django-admin startproject cafecompao`

### Aplicação Django
- Entrar na pasta criada do projeto: `cd cafecompao`
- Criar aplicação Django: 
`python manage.py startapp padarias` ou `py manage.py startapp padarias`
- Adicionar aplicação ao projeto em `cafecompao/settings.py`

```python
	INSTALLED_APPS = [
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'padarias',  # adicionar essa linha
]
``` 

- Verificar se está tudo ok rodando o servidor: `py manage.py runserver` e acessar a página `http://localhost:8000` no navegador


## Atividade 2 - Rotas e Arquivos Estáticos

1. Criar view e rota para a página inicial
2. Criar configuração de arquivos estáticos (CSS, JS, Imagens)
3. Criar página inicial a partir do protótipo do Café com Pão

### Resumo dos Conceitos Importantes
Nesta atividade vamos trabalhar dois conceitos importante *roteamento* e *gerenciamento de arquivos estáticos*. As rotas são responsáveis por mapear as URLs acessadas pelo usuário para o código que irá tratar dessa requisiçao. No django, as views são responsáveis por processar as requisições e retornar uma resposta ao usuário. No caso do Django, as views são funções que recebem um objeto `request` e retornam um objeto `response`.

Arquivos estáticos são arquivos que não se alteram em cada requisição tais como imagens, estilos e scripts. Esses arquivos podem ser servidos diretamente pelo servidor web sem a necessidade de processamento adicional. No Django, os arquivos estáticos são armazenados na pasta `static` e são servidos através de uma rota específica. Além disso, o Django possui uma configuração para servir arquivos de mídia (imagens, vídeos, etc) que são enviados pelos usuários. Em produção, arquivos estáticos e de mídia geralmente são armazenados em CDNs ou serviços de armazenamento em nuvem. [Ver mais sobre estáticos em Django.](https://docs.djangoproject.com/en/5.0/howto/static-files/)

### View e Rota Inicial
- Criar view `home` em `padarias/views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

- Criar rota para view `home` em `cafecompao/urls.py`

```python
from padarias import views  # adicionar esse import no início

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),   # adicionar essa linha
]
```

- Criar pasta `templates` na raiz do projeto com uma subpasta `padarias` e outra `components`
- Criar arquivo `home.html` em `templates/padarias` com uma página simples html para teste
- Adicionar configuração de templates em `cafecompao/settings.py`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': BASE_DIR / 'templates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- Rodar o servidor de desenvolvimento `py manage.py runserver` e acessar a página `http://localhost:8000/` no navegador e verificar se a página `home.html` é exibida corretamente

### Arquivos Estáticos
- Criar pasta `static` na raiz do projeto com subpastas `css`, `js` e `img`
- Copiar arquivos de estilo, scripts e imagens do protótipo do Café com Pão que estão na pasta `prototipo` no repositorio do professor para as pastas `static/css`, `static/js` e `static/img` respectivamente
- Adicionar configuração de arquivos estáticos e de media em `cafecompao/settings.py`

```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

- Configurar as rotas de arquivos estáticos e de pulmão em `cafecompao/urls.py`

```python   
# adicionar essas duas linhas no inicio do arquivo
# importando as funções necessárias para servir arquivos estáticos e de mídia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
] 
# adicionar essas duas linhas ao final que definem as rotas 
# de arquivo estaticos e de mídia
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- Copiar o conteudo do arquivo do protótipo 'prototipo/index.html' para o arquivo 'templates/home.html' e rodar o servidor de desenvolvimento `py manage.py runserver` e acessar a página `http://localhost:8000/` no navegador e verificar se a página `home.html` é exibida corretamente com os estilos e imagens do protótipo


