# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-24 15:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(verbose_name='Coment\xe1rio')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de cria\xe7\xe3o')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=models.TextField(verbose_name='conte\xfado'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=1024, verbose_name='T\xedtulo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usu\xe1rio'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usu\xe1rio'),
        ),
    ]