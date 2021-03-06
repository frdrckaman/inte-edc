# Generated by Django 3.0.9 on 2020-09-12 14:46

import uuid

import _socket
import django.contrib.sites.managers
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.fields.duration
import edc_model.models.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0007_auto_20200910_1742"),
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inte_subject", "0053_auto_20200910_2201"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComplicationsFollowup",
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
                            edc_model.models.validators.date.datetime_not_future,
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
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="INCOMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                (
                    "crf_status_comments",
                    models.TextField(
                        blank=True,
                        help_text="for example, why some data is still pending",
                        null=True,
                        verbose_name="Any comments related to status of this CRF",
                    ),
                ),
                (
                    "stroke",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Stroke",
                    ),
                ),
                (
                    "stroke_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "heart_attack",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Heart attack / heart failure",
                    ),
                ),
                (
                    "heart_attack_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "renal_disease",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Renal (kidney) disease",
                    ),
                ),
                (
                    "renal_disease_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "vision",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Vision problems (e.g. blurred vision)",
                    ),
                ),
                (
                    "vision_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "numbness",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Numbness / burning sensation",
                    ),
                ),
                (
                    "numbness_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "foot_ulcers",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Foot ulcers",
                    ),
                ),
                (
                    "foot_ulcers_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "complications",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        max_length=25,
                        verbose_name="Are there any other major complications to report?",
                    ),
                ),
                (
                    "complications_other",
                    models.TextField(blank=True, help_text="Please include dates", null=True),
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
                "verbose_name": "Complications: Followup",
                "verbose_name_plural": "Complications: Followup",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalComplicationsFollowup",
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
                            edc_model.models.validators.date.datetime_not_future,
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
                    "crf_status",
                    models.CharField(
                        choices=[
                            ("INCOMPLETE", "Incomplete (some data pending)"),
                            ("COMPLETE", "Complete"),
                        ],
                        default="INCOMPLETE",
                        help_text="If some data is still pending, flag this CRF as incomplete",
                        max_length=25,
                        verbose_name="CRF status",
                    ),
                ),
                (
                    "crf_status_comments",
                    models.TextField(
                        blank=True,
                        help_text="for example, why some data is still pending",
                        null=True,
                        verbose_name="Any comments related to status of this CRF",
                    ),
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
                    "stroke",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Stroke",
                    ),
                ),
                (
                    "stroke_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "heart_attack",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Heart attack / heart failure",
                    ),
                ),
                (
                    "heart_attack_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "renal_disease",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Renal (kidney) disease",
                    ),
                ),
                (
                    "renal_disease_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "vision",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Vision problems (e.g. blurred vision)",
                    ),
                ),
                (
                    "vision_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "numbness",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Numbness / burning sensation",
                    ),
                ),
                (
                    "numbness_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "foot_ulcers",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=25,
                        verbose_name="Foot ulcers",
                    ),
                ),
                (
                    "foot_ulcers_date",
                    models.DateField(
                        blank=True,
                        help_text="If exact date not known, see SOP on how to estimate a date.",
                        null=True,
                        verbose_name="If yes, date",
                    ),
                ),
                (
                    "complications",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        max_length=25,
                        verbose_name="Are there any other major complications to report?",
                    ),
                ),
                (
                    "complications_other",
                    models.TextField(blank=True, help_text="Please include dates", null=True),
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
                "verbose_name": "historical Complications: Followup",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name="clinicalreview",
            name="complications",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                help_text="If Yes, complete the `Complications` CRF",
                max_length=15,
                verbose_name="Since last seen, has the patient had any complications",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="historicalclinicalreview",
            name="complications",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                default="No",
                help_text="If Yes, complete the `Complications` CRF",
                max_length=15,
                verbose_name="Since last seen, has the patient had any complications",
            ),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name="complicationsfollowup",
            index=models.Index(
                fields=["subject_visit", "site", "id"],
                name="inte_subjec_subject_c92cd4_idx",
            ),
        ),
    ]
