# Generated by Django 4.0.4 on 2022-07-04 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro_website', '0006_blog_publishinguser_comment_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='CommentPost',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='PublishingUser',
        ),
    ]