# Generated by Django 5.1.4 on 2025-03-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f5', models.CharField(max_length=30)),
                ('f6', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parent1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=30)),
                ('f2', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parent2',
            fields=[
                ('f3', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('f4', models.CharField(max_length=30)),
            ],
        ),
    ]
