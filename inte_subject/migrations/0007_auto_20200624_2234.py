# Generated by Django 3.0.6 on 2020-06-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0006_auto_20200624_0627"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalhypertensioninitialreview",
            name="med_start_estimated_date",
            field=models.DateField(
                editable=False,
                null=True,
                verbose_name="Estimated medication start date",
            ),
        ),
        migrations.AlterField(
            model_name="hypertensioninitialreview",
            name="med_start_estimated_date",
            field=models.DateField(
                editable=False,
                null=True,
                verbose_name="Estimated medication start date",
            ),
        ),
    ]
