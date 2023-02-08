# Generated by Django 4.1.5 on 2023-02-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0007_remove_noticia_autor_noticia_autor_noticia_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='autor_noticia',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='autor_noticia',
        ),
        migrations.AddField(
            model_name='autor',
            name='autor_noticia',
            field=models.CharField(default='Anonimo', max_length=50),
        ),
        migrations.AddField(
            model_name='noticia',
            name='autor_noticia',
            field=models.ManyToManyField(to='Noticias.autor'),
        ),
    ]
