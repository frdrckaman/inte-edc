# Generated by Django 3.1.6 on 2021-02-05 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inte_consent", "0006_auto_20210203_0706"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalsubjectconsent",
            options={
                "get_latest_by": "history_date",
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Subject Consent",
            },
        ),
        migrations.AlterModelOptions(
            name="subjectconsent",
            options={
                "get_latest_by": "consent_datetime",
                "ordering": ("created",),
                "verbose_name": "Subject Consent",
                "verbose_name_plural": "Subject Consents",
            },
        ),
    ]
