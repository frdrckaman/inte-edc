# Generated by Django 3.0.9 on 2020-10-20 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0008_auto_20201002_0403"),
        ("edc_action_item", "0026_auto_20200729_2240"),
        ("inte_subject", "0073_auto_20201007_2106"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="historicalsubjectvisitmissed",
            name="crf_status",
        ),
        migrations.RemoveField(
            model_name="historicalsubjectvisitmissed",
            name="crf_status_comments",
        ),
        migrations.RemoveField(
            model_name="subjectvisitmissed",
            name="crf_status",
        ),
        migrations.RemoveField(
            model_name="subjectvisitmissed",
            name="crf_status_comments",
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="action_identifier",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="action_item_reason",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="ltfu",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="No",
                help_text="If 'Yes', complete the Loss to Follow up form",
                max_length=15,
                verbose_name="Has the participant met the protocol criteria for lost to follow up?",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="parent_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="parent_action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="related_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisitmissed",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="action_identifier",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="action_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="action_item_reason",
            field=models.TextField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="ltfu",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                default="No",
                help_text="If 'Yes', complete the Loss to Follow up form",
                max_length=15,
                verbose_name="Has the participant met the protocol criteria for lost to follow up?",
            ),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="parent_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="parent_action_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="related_action_identifier",
            field=models.CharField(
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="related_action_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.ActionItem",
            ),
        ),
        migrations.AddField(
            model_name="subjectvisitmissed",
            name="tracking_identifier",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="info_source",
            field=models.CharField(
                choices=[
                    ("hospital_notes", "Hospital notes"),
                    ("outpatient_cards", "Outpatient cards"),
                    ("patient", "Patient"),
                    (
                        "patient_and_outpatient",
                        "Patient, hospital notes and/or outpatient card",
                    ),
                    ("collateral_history", "Collateral History from relative/guardian"),
                    ("N/A", "Not applicable"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What is the main source of this information?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="reason",
            field=models.CharField(
                choices=[
                    ("scheduled", "Scheduled visit (study)"),
                    ("unscheduled", "Routine / Unscheduled visit (non-study)"),
                    ("missed", "Missed visit"),
                ],
                help_text="Only baseline (0m), 6m and 12m are considered `scheduled` visits as per the INTE protocol.If `missed' complete CRF Missed Visit Report.",
                max_length=25,
                verbose_name="What is the reason for this visit report?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisitmissed",
            name="survival_status",
            field=models.CharField(
                choices=[
                    ("alive", "Alive"),
                    ("dead", "Deceased"),
                    ("unknown", "Unknown"),
                ],
                help_text="If deceased, complete the death report",
                max_length=25,
                verbose_name="Survival status",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="info_source",
            field=models.CharField(
                choices=[
                    ("hospital_notes", "Hospital notes"),
                    ("outpatient_cards", "Outpatient cards"),
                    ("patient", "Patient"),
                    (
                        "patient_and_outpatient",
                        "Patient, hospital notes and/or outpatient card",
                    ),
                    ("collateral_history", "Collateral History from relative/guardian"),
                    ("N/A", "Not applicable"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What is the main source of this information?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="reason",
            field=models.CharField(
                choices=[
                    ("scheduled", "Scheduled visit (study)"),
                    ("unscheduled", "Routine / Unscheduled visit (non-study)"),
                    ("missed", "Missed visit"),
                ],
                help_text="Only baseline (0m), 6m and 12m are considered `scheduled` visits as per the INTE protocol.If `missed' complete CRF Missed Visit Report.",
                max_length=25,
                verbose_name="What is the reason for this visit report?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisitmissed",
            name="survival_status",
            field=models.CharField(
                choices=[
                    ("alive", "Alive"),
                    ("dead", "Deceased"),
                    ("unknown", "Unknown"),
                ],
                help_text="If deceased, complete the death report",
                max_length=25,
                verbose_name="Survival status",
            ),
        ),
    ]
