# Generated by Django 4.0.4 on 2022-07-04 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_website', '0004_rename_imgaen_avatar_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='imagen',
        ),
    ]
