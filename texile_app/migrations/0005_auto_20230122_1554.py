# Generated by Django 3.2.3 on 2023-01-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texile_app', '0004_auto_20230122_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='y_data_hourly',
            name='update_time',
        ),
        migrations.AddField(
            model_name='y_data_hourly',
            name='chart_type',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='y_data_hourly',
            name='chart',
            field=models.CharField(default='', max_length=10),
        ),
    ]
