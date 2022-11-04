# Generated by Django 4.1.2 on 2022-11-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionScrapers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullHard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='venex',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='venex',
            name='category',
        ),
    ]
