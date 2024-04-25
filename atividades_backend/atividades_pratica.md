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


## Atividade 3 - Bancos de Dados e ORM 

1. Criar modelo de dados para `Categoria`
2. Criar o migration
3. Carregar as fixtures de categoria
4. Verificar se as categorias foram carregadas corretamente com sqlite browser

### Resumo dos Conceitos Importantes

Nesta atividade vamos trabalhar com bancos de dados e o ORM (Object Relational Mapping). O ORM é uma técnica de mapeamento de objetos para tabelas de banco de dados relacionais. O ORM permite que o desenvolvedor utilize objetos e métodos para manipular dados no banco de dados sem a necessidade de escrever SQL diretamente. Além de abstrair a comunicação com o banco de dados, o ORM facilita o desenvolvimento de consultas e lida com diversos aspectos como segurança, otimização, migrações e consistência dos dados.

O Django possui um ORM poderoso que permite a criação de modelos de dados, consultas complexas e migrações de banco de dados de forma simples e eficiente. [Ver mais sobre ORM em Django.](https://docs.djangoproject.com/en/5.0/topics/db/models/)

Outros conceitos que vamos ver é o de migrations e fixtures. Migrations são arquivos que contém as alterações no banco de dados e são gerados pelo ORM sempre que existe alguma alteração no modelo de dados. As migrations representam as alterações no banco de dados e portanto são versionadas e podem ser revertidas. Fixtures são arquivos que contém dados iniciais para popular o banco de dados. Fixtures são úteis para popular o banco de dados com dados de teste ou dados iniciais para a aplicação (dados de configuração).

### Modelo de Dados

- Vamos inicialmente o seguinte modelo de dados do Café com Pão na imagem abaixo:
- Vamos implementar inicialmente sem considerar a necessidade do usuário realizar as assinaturas de cestas diretamente no site. Vamos divulgar somente as cestas, produtos e as padarias e caso o cliente deseja, ele pode entrar em contato com qualquer uma das padarias da rede e continuar a assinatura diretamente com a padaria.

![Modelo de Dados](erd.png)

### Criar Model de Padaria

- Models são classes que representam as tabelas do banco de dados. Cada atributo da classe representa uma coluna da tabela. O Django possui diversos tipos de campos que representam os tipos de dados do banco de dados. [Ver mais sobre modelos de dados em Django.](https://docs.djangoproject.com/en/5.0/topics/db/models/#fields)
- Criar modelo de dados para `Categoria` em `padarias/models.py`

```python
class Categoria(models.Model):
    nome = models.CharField(
        verbose_name="Nome", max_length=100, unique=True, null=False, blank=False, help_text="Nome da categoria")

    def __str__(self):
        return self.nome
``` 

### Criar Migration

- Criar migration automaticamente para o modelo de dados `Categoria` com o comando `py manage.py makemigrations`
- Verificar que o arquivo de migration foi criado em `padarias/migrations`

```python
from django.db import migrations, models
 
class Migration(migrations.Migration):
 
    initial = True
 
    dependencies = [
    ]
 
    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da categoria', max_length=100, unique=True, verbose_name='Nome')),
            ],
        ),
    ]
```

- Aplicar a migration com o comando `py manage.py migrate`
- Saída esperada:

```bash
python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, padarias, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying padarias.0001_initial... OK
  Applying sessions.0001_initial... OK
```

### Criar e carregar Fixtures

- Criar arquivo `categorias.json` na pasta `padarias/fixtures` com os dados de categorias
- Fixtures no django possuem um formato específico que é um array de objetos json onde cada objeto representa um registro da tabela. [Ver mais sobre fixtures em Django.](https://docs.djangoproject.com/en/5.0/howto/initial-data/)

```json
[
    {
        "model": "padarias.categoria",
        "pk": 1,
        "fields": {
            "nome": "Frutas"
        }
    },
    {
        "model": "padarias.categoria",
        "pk": 2,
        "fields": {
            "nome": "Bebidas"
        }
    },
    {
        "model": "padarias.categoria",
        "pk": 3,
        "fields": {
            "nome": "Pães"
        }
    },
    {
        "model": "padarias.categoria",
        "pk": 4,
        "fields": {
            "nome": "Salgados"
        }
    },
    {
        "model": "padarias.categoria",
        "pk": 5,
        "fields": {
            "nome": "Biscoitos"
        }
    }
]
```

- Carregar as fixtures com o comando `py manage.py loaddata categorias`

### Verificar Dados no Banco de Dados

- Verificar se as categorias foram carregadas corretamente com o sqlite browser
- Instalar o sqlite browser: https://sqlitebrowser.org/dl/
- Abrir o arquivo `db.sqlite3` que esta na raiz do projeto com o sqlite browser e verificar se as categorias foram carregadas corretamente
- Existe uma extensão no VS Code chamada `SQLite` que também pode ser utilizada para visualizar o banco de dados

### Atividade em Aula
- Reproduzir os passos acima
- Enviar para github com mensagem de commit 'Atividade 3 - Bancos de Dados e ORM parte 1'

## Atividade 4 - Bancos de Dados e ORM - Parte 2 

1. Incluir dependência para lidar com imagens no Django ( lib 'Pillow' )
2. Criar modelo de dados para `Cesta` e `Produto` e os relacionamentos entre eles
3. Criar e aplicar migrations
4. Criar e aplicar fixtures.

### Resumo dos Conceitos Importantes
Nesta atividade vamos trabalhar alguns conceitos importantes relacionado a ORM: como representar relacionamento entre tabelas e como representar os diferentes tipos de dados. Em SGBDs relacionais temos 3 tipos de relacionamentos: 1 para 1, 1 para N e N para N. No Django, os relacionamentos entre modelos são representados por campos especiais que representam a relação entre as tabelas. Os tipos de relacionamentos mais comuns são: `ForeignKey`, `ManyToManyField` e `OneToOneField`. [Ver mais sobre relacionamentos em Django.](https://docs.djangoproject.com/en/5.0/topics/db/models/)

Os bancos de dados relacionais possuem diversos tipos de dados que representam os diferentes tipos de dados que podem ser armazenados. No Django, os tipos de dados são representados por campos que representam os tipos de dados do banco de dados. Além dos tipos de dados padrão do banco de dados, o Django possui campos especiais para armazenar arquivos, imagens, JSON, etc. [Ver mais sobre tipos de dados em Django.](https://docs.djangoproject.com/en/5.0/ref/models/fields/). Nesta atividade vamos incluir o tipo de campo para represenar imagens no modelo de dados de `Padaria` e `Cesta` que possui a lib de dependencia chamada Pillow.

### Incluir dependência para lidar com imagens no Django
- Instalar Pillow: `pip install Pillow` ou `py -m pip install Pillow`

### Criar Model de Cesta e Produto
- No arquivo `models.py` criar o model de Cesta e Produto segundo o ERD da atividade anterior.
- Olhando o ERD o model de `Produto` deve ter um relacionamento `ManyToMany` com `Cesta` e um relacionamento `ForeignKey` com `Categoria`
- No arquivo `models.py`

```python
import uuid # colocar essa linha no inicio do arquivo

class Produto(models.Model):
    nome = models.CharField(
        verbose_name="Nome", max_length=100, unique=True, null=False, blank=False, help_text="Nome do produto")
    descricao = models.TextField(
        verbose_name="Descrição", null=True, blank=True, help_text="Descrição do produto")
    preco = models.DecimalField(
        verbose_name="Preço", max_digits=10, decimal_places=2, null=False, blank=False, help_text="Preço do produto")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, verbose_name="Categoria", null=True, help_text="Categoria do produto")

    def __str__(self):
        return self.nome


class Cesta(models.Model):

    class Niveis(models.TextChoices):
        BASICO = 'B', 'Básico'
        MEDIO = 'M', 'Médio'
        PREMIUM = 'P', 'Premium'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(
        verbose_name="Nome", max_length=100, unique=True, null=False, blank=False, help_text="Nome da cesta")
    descricao = models.TextField(
        verbose_name="Descrição", null=True, blank=True, help_text="Descrição da cesta")
    preco = models.DecimalField(
        verbose_name="Preço", max_digits=10, decimal_places=2, null=False, blank=False, help_text="Preço da cesta")
    produtos = models.ManyToManyField(
        Produto, verbose_name="Produtos", help_text="Produtos da cesta", related_name="cestas")
    nivel = models.CharField(
        verbose_name="Nível", max_length=1, choices=Niveis.choices, default=Niveis.BASICO, help_text="Nível da cesta")
    imagem = models.ImageField(
        verbose_name="Imagem", upload_to="cestas", null=True, blank=True, help_text="Imagem da cesta")

    def __str__(self):
        return self.nome
```

#### Observações 

- Verifique que os relacionamentos foram criados com os campos ManyToManyField referenciando a tabela de produtos e ForeignKey referenciando a tabela de categorias.
- No caso de Cesta, gostariamos de criar os Níveis de cestas. Esse tipo de padrão é comum, sempre que queremos definir tipos de dados que são fixos e não devem ser alterados. Em diversos frameworks esse tipo de padrão é chamado de `Enum`. 
- O método `__str__` é um método especial que retorna uma representação em string do objeto. Funciona como o toString do Java.
- O campo `id` é criado automaticamente como um inteiro autoincremental. No caso do model Cesta, o `id` foi criado como um campo UUIDField que é um campo que gera um identificador único universal. Esse campo é útil para garantir que o identificador seja único em diferentes bases de dados. Existem diversas vantagens e desvantagens para representar o `id` de diferentes formas. [Ver mais sobre UUID em Django.](https://docs.djangoproject.com/en/5.0/ref/models/fields/#uuidfield). 

### Criar e Aplicar Migrations

- Criar migration automaticamente para os modelos de dados `Cesta` e `Produto` com o comando `py manage.py makemigrations`
- Verificar que novos arquivos de migration foram criados em `padarias/migrations`
- Aplicar a migration com o comando `py manage.py migrate`

```bash
❯ python manage.py makemigrations
Migrations for 'padarias':
  padarias/migrations/0002_produto_cesta.py
    - Create model Produto
    - Create model Cesta

❯ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, padarias, sessions
Running migrations:
  Applying padarias.0002_produto_cesta... OK
```

### Criar e Carregar Fixtures
- Copiar os arquivos `produtos.json` e `cestas.json` da pasta `prototipo/fixtures` para a pasta `padarias/fixtures` que contem os dados iniciais de produtos e cestas
- Veja que nos arquivos de fixtures os produtos e cestas estão relacionados com as categorias que foram criadas anteriormente e entre si também. Dessa forma é possível pré-definir esses relacionamentos por meio das fixtures.
- Carregar as fixtures com o comando `py manage.py loaddata produtos` e `py manage.py loaddata cestas` nesta ordem
- Verificar se os produtos e cestas foram carregadas corretamente com o sqlite browser ou via extensao do VS Code

```bash
❯ python manage.py loaddata produtos
Installed 24 object(s) from 1 fixture(s)
❯ python manage.py loaddata cestas
Installed 3 object(s) from 1 fixture(s)
```

### Atividade na Aula
- Reproduzir os passos acima
- Implementar os models restantes (Padaria e Endereço) e os relacionamentos entre eles assim como as migrations e fixtures correspondentes
- Enviar para o github com mensagem de commit 'Atividade 4 - Banco de dados e ORM parte 2'




