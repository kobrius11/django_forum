# Generated by Django 4.2.5 on 2023-09-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='please provide post title', max_length=500, verbose_name='title'),
        ),
    ]