# Generated by Django 5.0.4 on 2024-04-29 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('instrutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos_ministrados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('order', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='cursos.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Licao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licoes', to='cursos.modulo')),
            ],
        ),
    ]
