# Generated by Django 3.0.4 on 2020-04-04 17:55

import _socket
from django.conf import settings
import django.contrib.sites.managers
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inte_subject", "0025_auto_20200404_2028"),
    ]

    operations = [
        migrations.CreateModel(
            name="HealthRiskAssessment",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "smoking_status",
                    models.CharField(
                        choices=[
                            ("smoker", "Currently smoke"),
                            ("former_smoker", "Used to smoke but stopped"),
                            ("nonsmoker", "Never smoked"),
                        ],
                        max_length=15,
                        verbose_name="Which of these options describes you",
                    ),
                ),
                (
                    "smoker_quit_ago_str",
                    models.CharField(
                        blank=True,
                        help_text="Duration since last smoked. Format is `YYyMMm`. For example 1y11m, 12y7m, etc",
                        max_length=8,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^([0-9]{1,3}y([0-5]?[0-9]m)?)$",
                                message="Invalid format. Expected something like 3y5m, 1y0m, etc",
                            )
                        ],
                        verbose_name="If you used to smoke but stopped, how long ago did you stop",
                    ),
                ),
                ("smoker_quit_ago_months", models.IntegerField(editable=False)),
                (
                    "alcohol",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Do you drink alcohol?",
                    ),
                ),
                (
                    "alcohol_consumption",
                    models.CharField(
                        choices=[
                            ("ocassionally", "Ocassionally"),
                            ("1_2_per_week", "1-2 times a week"),
                            ("3_4_per_week", "3-4 times a week"),
                            ("daily", "Daily"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=25,
                        verbose_name="If yes, how often do you drink alcohol?",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inte_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Health Risk Assessment",
                "verbose_name_plural": "Health Risk Assessments",
                "abstract": False,
            },
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalHealthRiskAssessment",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "smoking_status",
                    models.CharField(
                        choices=[
                            ("smoker", "Currently smoke"),
                            ("former_smoker", "Used to smoke but stopped"),
                            ("nonsmoker", "Never smoked"),
                        ],
                        max_length=15,
                        verbose_name="Which of these options describes you",
                    ),
                ),
                (
                    "smoker_quit_ago_str",
                    models.CharField(
                        blank=True,
                        help_text="Duration since last smoked. Format is `YYyMMm`. For example 1y11m, 12y7m, etc",
                        max_length=8,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^([0-9]{1,3}y([0-5]?[0-9]m)?)$",
                                message="Invalid format. Expected something like 3y5m, 1y0m, etc",
                            )
                        ],
                        verbose_name="If you used to smoke but stopped, how long ago did you stop",
                    ),
                ),
                ("smoker_quit_ago_months", models.IntegerField(editable=False)),
                (
                    "alcohol",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Do you drink alcohol?",
                    ),
                ),
                (
                    "alcohol_consumption",
                    models.CharField(
                        choices=[
                            ("ocassionally", "Ocassionally"),
                            ("1_2_per_week", "1-2 times a week"),
                            ("3_4_per_week", "3-4 times a week"),
                            ("daily", "Daily"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=25,
                        verbose_name="If yes, how often do you drink alcohol?",
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="inte_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Health Risk Assessment",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(model_name="riskfactors", name="site",),
        migrations.RemoveField(model_name="riskfactors", name="subject_visit",),
        migrations.DeleteModel(name="HistoricalRiskFactors",),
        migrations.DeleteModel(name="RiskFactors",),
        migrations.AddIndex(
            model_name="healthriskassessment",
            index=models.Index(
                fields=["subject_visit", "site", "id"],
                name="inte_subjec_subject_ea9ec4_idx",
            ),
        ),
    ]