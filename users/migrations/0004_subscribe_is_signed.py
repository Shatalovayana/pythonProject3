# Generated by Django 4.2.9 on 2024-02-22 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='is_signed',
            field=models.BooleanField(blank=True, null=True, verbose_name='подписан ли пользователь'),
        ),
    ]
