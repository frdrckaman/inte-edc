# Generated by Django 3.1.5 on 2021-02-03 17:09

import django.db.models.deletion
import edc_model.models.validators.date
import edc_model_fields.fields.other_charfield
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_adverse_event", "0005_auto_20210120_0005"),
        ("edc_action_item", "0028_auto_20210203_0706"),
        ("inte_ae", "0005_auto_20210120_0005"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="deathreport",
            options={
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
                "get_latest_by": "modified",
                "ordering": ("-modified", "-created"),
                "verbose_name": "Death Report",
            },
        ),
        migrations.AddField(
            model_name="deathreport",
            name="cause_of_death",
            field=models.ForeignKey(
                editable=False,
                help_text="Main cause of death in the opinion of the local study doctor and local PI",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_adverse_event.causeofdeath",
                verbose_name="Main cause of death",
            ),
        ),
        migrations.AddField(
            model_name="deathreport",
            name="cause_of_death_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="deathreport",
            name="death_as_inpatient",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Death as inpatient",
            ),
        ),
        migrations.AddField(
            model_name="deathreport",
            name="study_day",
            field=models.IntegerField(
                editable=False,
                help_text="This field is not used",
                null=True,
                verbose_name="Study day",
            ),
        ),
        migrations.AddField(
            model_name="historicaldeathreport",
            name="cause_of_death",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                help_text="Main cause of death in the opinion of the local study doctor and local PI",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_adverse_event.causeofdeath",
                verbose_name="Main cause of death",
            ),
        ),
        migrations.AddField(
            model_name="historicaldeathreport",
            name="cause_of_death_other",
            field=edc_model_fields.fields.other_charfield.OtherCharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="If other, please specify ...",
            ),
        ),
        migrations.AddField(
            model_name="historicaldeathreport",
            name="death_as_inpatient",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=5,
                null=True,
                verbose_name="Death as inpatient",
            ),
        ),
        migrations.AddField(
            model_name="historicaldeathreport",
            name="study_day",
            field=models.IntegerField(
                editable=False,
                help_text="This field is not used",
                null=True,
                verbose_name="Study day",
            ),
        ),
        migrations.AlterField(
            model_name="aefollowup",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="aefollowup",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aefollowup",
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
            model_name="aefollowup",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aefollowup",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
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
            model_name="aeinitial",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aeinitial",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="aesusar",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="aesusar",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aesusar",
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
            model_name="aesusar",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aesusar",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="aetmg",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="aetmg",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aetmg",
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
            model_name="aetmg",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="aetmg",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="deathreport",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="deathreport",
            name="death_date",
            field=models.DateField(
                null=True,
                validators=[edc_model.models.validators.date.date_not_future],
                verbose_name="Date of Death",
            ),
        ),
        migrations.AlterField(
            model_name="deathreport",
            name="narrative",
            field=models.TextField(
                help_text="Provide any additional details, if relevant",
                null=True,
                verbose_name="Comment",
            ),
        ),
        migrations.AlterField(
            model_name="deathreport",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="deathreport",
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
            model_name="deathreport",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="deathreport",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="deathreporttmg",
            name="action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="deathreporttmg",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="deathreporttmg",
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
            model_name="deathreporttmg",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="deathreporttmg",
            name="related_action_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="edc_action_item.actionitem",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaefollowup",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalaefollowup",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalaesusar",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalaesusar",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalaetmg",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalaetmg",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreport",
            name="death_date",
            field=models.DateField(
                null=True,
                validators=[edc_model.models.validators.date.date_not_future],
                verbose_name="Date of Death",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreport",
            name="narrative",
            field=models.TextField(
                help_text="Provide any additional details, if relevant",
                null=True,
                verbose_name="Comment",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreport",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreport",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreporttmg",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreporttmg",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreporttmgsecond",
            name="parent_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to parent reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicaldeathreporttmgsecond",
            name="related_action_identifier",
            field=models.CharField(
                blank=True,
                help_text="action identifier that links to related reference model instance.",
                max_length=30,
                null=True,
            ),
        ),
    ]
