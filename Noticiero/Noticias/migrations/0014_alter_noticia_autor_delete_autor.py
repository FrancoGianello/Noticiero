# Generated by Django 4.1.5 on 2023-02-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0013_remove_noticia_autor_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.CharField(default='francis', max_length=50),
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
    ]
