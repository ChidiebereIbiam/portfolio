# Generated by Django 4.1 on 2023-08-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_title_project_project_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
