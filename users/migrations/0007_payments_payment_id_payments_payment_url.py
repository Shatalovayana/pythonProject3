# Generated by Django 4.2.9 on 2024-02-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_payments_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id сессии оплаты'),
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_url',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='Ссылка на оплату'),
        ),
    ]
