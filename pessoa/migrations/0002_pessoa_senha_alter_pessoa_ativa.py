# Generated by Django 4.0.3 on 2022-03-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='senha',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='ativa',
            field=models.CharField(max_length=50),
        ),
    ]
