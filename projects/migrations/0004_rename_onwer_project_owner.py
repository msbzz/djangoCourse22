# Generated by Django 4.0.5 on 2022-06-14 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_onwer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='onwer',
            new_name='owner',
        ),
    ]