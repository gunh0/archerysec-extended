# Generated by Django 3.1.2 on 2020-10-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_auto_20201006_0027"),
    ]

    operations = [
        migrations.AddField(
            model_name="project_db",
            name="total_medium",
            field=models.TextField(null=True),
        ),
    ]
