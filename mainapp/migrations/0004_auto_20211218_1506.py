# Generated by Django 3.2.9 on 2021-12-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20211208_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
