# Generated by Django 5.1.4 on 2025-03-02 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_employee_delete_child_delete_parent1_delete_parent2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='address',
            new_name='eaddr',
        ),
    ]
