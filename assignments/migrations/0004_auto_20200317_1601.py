# Generated by Django 3.0.4 on 2020-03-17 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0003_auto_20200315_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='available_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
