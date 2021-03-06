# Generated by Django 4.0.4 on 2022-07-04 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_website', '0002_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('contenido', models.CharField(max_length=35000)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='proyectos')),
                ('autor', models.CharField(max_length=40)),
                ('resumen', models.CharField(max_length=5000)),
            ],
        ),
    ]
