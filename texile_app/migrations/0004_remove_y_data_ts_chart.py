# Generated by Django 3.2.3 on 2023-01-24 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('texile_app', '0003_y_data_ts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='y_data_ts',
            name='chart',
        ),
    ]