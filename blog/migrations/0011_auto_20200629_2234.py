# Generated by Django 2.2.13 on 2020-06-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
