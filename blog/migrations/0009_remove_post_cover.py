# Generated by Django 2.2.13 on 2020-06-25 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
    ]
