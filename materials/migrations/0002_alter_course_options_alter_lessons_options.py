# Generated by Django 4.2.9 on 2024-02-09 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'курс', 'verbose_name_plural': 'курсы'},
        ),
        migrations.AlterModelOptions(
            name='lessons',
            options={'verbose_name': 'урок', 'verbose_name_plural': 'уроки'},
        ),
    ]