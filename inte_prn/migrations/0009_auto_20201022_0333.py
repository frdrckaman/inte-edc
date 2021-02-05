# Generated by Django 3.0.9 on 2020-10-22 00:33

import edc_utils.date
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_prn", "0008_auto_20201022_0048"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicallosstofollowup",
            name="ltfu_date",
            field=models.DateField(
                default=edc_utils.date.get_utcnow,
                null=True,
                verbose_name="Date participant considered lost to follow up",
            ),
        ),
        migrations.AddField(
            model_name="historicallosstofollowuphiv",
            name="ltfu_date",
            field=models.DateField(
                default=edc_utils.date.get_utcnow,
                null=True,
                verbose_name="Date participant considered lost to follow up",
            ),
        ),
        migrations.AddField(
            model_name="historicallosstofollowupncd",
            name="ltfu_date",
            field=models.DateField(
                default=edc_utils.date.get_utcnow,
                null=True,
                verbose_name="Date participant considered lost to follow up",
            ),
        ),
        migrations.AddField(
            model_name="losstofollowup",
            name="ltfu_date",
            field=models.DateField(
                default=edc_utils.date.get_utcnow,
                null=True,
                verbose_name="Date participant considered lost to follow up",
            ),
        ),
    ]
