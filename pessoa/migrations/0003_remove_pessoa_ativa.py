# Generated by Django 4.0.3 on 2022-03-22 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_pessoa_senha_alter_pessoa_ativa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='ativa',
        ),
    ]
