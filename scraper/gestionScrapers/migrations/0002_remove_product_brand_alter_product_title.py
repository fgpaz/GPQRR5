# Generated by Django 4.1.3 on 2022-11-12 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionScrapers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Producto-Titulo'),
        ),
    ]
