# Generated by Django 4.2.9 on 2024-03-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_payments_payment_id_payments_payment_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id продукта'),
        ),
    ]
