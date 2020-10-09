# Generated by Django 3.1.2 on 2020-10-08 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20201007_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_db',
            name='high_net',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project_db',
            name='high_static',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project_db',
            name='high_web',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project_db',
            name='low_net',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project_db',
            name='low_static',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project_db',
            name='low_web',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project_db',
            name='medium_net',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project_db',
            name='medium_static',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project_db',
            name='medium_web',
            field=models.TextField(null=True),
        ),
    ]
