# Generated by Django 3.0.4 on 2020-03-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=30)),
                ('institution', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]