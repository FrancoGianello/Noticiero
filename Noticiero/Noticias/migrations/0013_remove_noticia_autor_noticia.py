# Generated by Django 4.1.5 on 2023-02-06 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0012_remove_noticia_autor_noticia_noticia_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='autor_noticia',
        ),
    ]
