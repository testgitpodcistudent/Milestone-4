# Generated by Django 3.2.3 on 2021-11-21 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]