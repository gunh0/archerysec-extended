# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-07 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tools", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="nikto_vuln_db",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vuln_id", models.UUIDField(blank=True, null=True)),
                ("scan_id", models.UUIDField(blank=True, null=True)),
                ("project_id", models.TextField(blank=True, null=True)),
                ("scan_url", models.TextField(blank=True, null=True)),
                ("discription", models.TextField(blank=True, null=True)),
                ("targetip", models.TextField(blank=True, null=True)),
                ("hostname", models.TextField(blank=True, null=True)),
                ("port", models.TextField(blank=True, null=True)),
                ("uri", models.TextField(blank=True, null=True)),
                ("httpmethod", models.TextField(blank=True, null=True)),
                ("testlinks", models.TextField(blank=True, null=True)),
                ("osvdb", models.TextField(blank=True, null=True)),
                ("false_positive", models.TextField(blank=True, null=True)),
                ("jira_ticket", models.TextField(blank=True, null=True)),
                ("vuln_status", models.TextField(blank=True, null=True)),
                ("dup_hash", models.TextField(blank=True, null=True)),
                ("vuln_duplicate", models.TextField(blank=True, null=True)),
                ("false_positive_hash", models.TextField(blank=True, null=True)),
                ("date_time", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="nikto_result_db",
            name="date_time",
            field=models.TextField(blank=True, null=True),
        ),
    ]
