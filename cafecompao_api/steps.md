# Templating

## settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'       <--------- INSERIR
        ],
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

- Criar pasta templates na raiz do projeto com subpastas 'components' e 'padarias'

## Configurando arquivos estáticos e de mídia

- Criar pasta 'static' e 'media' na raiz do projeto
- Criar configurações no settings.py




- Criar configurações no urls.py
