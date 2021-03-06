# Generated by Django 3.0.6 on 2020-07-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0016_auto_20200709_0819"),
    ]

    operations = [
        migrations.AlterField(
            model_name="otherbaselinedata",
            name="marital_status",
            field=models.CharField(
                choices=[
                    ("married", "Married or living with someone"),
                    ("single", "Single"),
                    ("divorced", "Divorced"),
                    ("widowed", "Widow / Spinster"),
                ],
                max_length=25,
                verbose_name="Personal status?",
            ),
        ),
    ]
