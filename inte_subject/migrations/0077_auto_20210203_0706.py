# Generated by Django 3.1.5 on 2021-02-03 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_action_item", "0028_auto_20210203_0706"),
        ("inte_subject", "0076_auto_20201123_0724"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="info_source",
            field=models.CharField(
                choices=[
                    ("patient", "Patient"),
                    (
                        "patient_and_outpatient",
                        "Patient, hospital notes and/or outpatient card",
                    ),
                    (
                        "patient_representive",
                        "Patient Representative (e.family member, friend)",
                    ),
                    ("hospital_notes", "Hospital notes"),
                    ("outpatient_cards", "Outpatient cards"),
                    ("collateral_history", "Collateral History from relative/guardian"),
                    ("N/A", "Not applicable"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What is the main source of this information?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisitmissed",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisitmissed",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="info_source",
            field=models.CharField(
                choices=[
                    ("patient", "Patient"),
                    (
                        "patient_and_outpatient",
                        "Patient, hospital notes and/or outpatient card",
                    ),
                    (
                        "patient_representive",
                        "Patient Representative (e.family member, friend)",
                    ),
                    ("hospital_notes", "Hospital notes"),
                    ("outpatient_cards", "Outpatient cards"),
                    ("collateral_history", "Collateral History from relative/guardian"),
                    ("N/A", "Not applicable"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What is the main source of this information?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisitmissed",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisitmissed",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisitmissed",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisitmissed",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisitmissed",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
    ]
