# Generated by Django 3.0.6 on 2020-07-14 13:54

import edc_model.models.fields.other_charfield
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0018_auto_20200713_2221"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalotherbaselinedata",
            name="employment_status_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="otherbaselinedata",
            name="employment_status_other",
            field=edc_model.models.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=35,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
    ]
