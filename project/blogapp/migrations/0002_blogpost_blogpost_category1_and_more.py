# Generated by Django 4.0.1 on 2022-04-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Blogpost_category1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Blogpost_category2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Blogpost_category3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Blogpost_category4',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Blogpost_category5',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Blogpost_category6',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Blogpost_picture1',
            field=models.ImageField(default='', upload_to='blogapp/images'),
        ),
    ]
