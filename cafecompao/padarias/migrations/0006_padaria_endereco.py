# Generated by Django 5.0.3 on 2024-05-01 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('padarias', '0005_remove_cesta_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Padaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da padaria', max_length=100, unique=True, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, help_text='Descrição da padaria', null=True, verbose_name='Descrição')),
                ('imagem', models.ImageField(blank=True, help_text='Imagem da padaria', null=True, upload_to='padarias', verbose_name='Imagem')),
                ('cestas', models.ManyToManyField(help_text='Cestas da padaria', related_name='padarias', to='padarias.cesta', verbose_name='Cestas')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(help_text='Rua do endereço', max_length=100, verbose_name='Rua')),
                ('numero', models.CharField(help_text='Número do endereço', max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, help_text='Complemento do endereço', max_length=100, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, help_text='Bairro do endereço', max_length=100, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(help_text='Cidade do endereço', max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(help_text='Estado do endereço', max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(help_text='CEP do endereço', max_length=8, verbose_name='CEP')),
                ('padaria', models.OneToOneField(help_text='Padaria do endereço', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='padarias.padaria', verbose_name='Padaria')),
            ],
        ),
    ]
