# Generated by Django 4.2.9 on 2024-03-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_course_owner_lessons_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=15000, verbose_name='стоимость курса'),
        ),
    ]
