# Generated by Django 4.1.5 on 2023-02-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('img1', models.ImageField(null=True, upload_to='')),
                ('img2', models.ImageField(null=True, upload_to='')),
                ('img3', models.ImageField(null=True, upload_to='')),
                ('img4', models.ImageField(null=True, upload_to='')),
                ('img5', models.ImageField(null=True, upload_to='')),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
