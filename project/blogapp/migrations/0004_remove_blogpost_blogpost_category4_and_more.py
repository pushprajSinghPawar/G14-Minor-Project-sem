# Generated by Django 4.0.1 on 2022-04-18 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blogpost_blogpost_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='Blogpost_category4',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='Blogpost_category5',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='Blogpost_category6',
        ),
    ]