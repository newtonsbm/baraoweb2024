# Generated by Django 5.0.3 on 2024-05-04 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('padarias', '0004_alter_assinatura_data_fim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assinatura',
            name='data_fim',
        ),
    ]
