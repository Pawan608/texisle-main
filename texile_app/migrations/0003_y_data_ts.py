# Generated by Django 3.2.3 on 2023-01-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texile_app', '0002_auto_20221228_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='y_data_ts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart', models.CharField(default='', max_length=10)),
                ('chart_type', models.CharField(default='', max_length=10)),
                ('data', models.CharField(default='', max_length=10)),
                ('date', models.CharField(default='', max_length=20)),
                ('time', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
