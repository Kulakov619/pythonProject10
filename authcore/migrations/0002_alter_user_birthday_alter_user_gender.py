# Generated by Django 4.2.5 on 2023-12-05 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authcore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.BooleanField(blank=True, null=True, verbose_name='мужчина?'),
        ),
    ]
