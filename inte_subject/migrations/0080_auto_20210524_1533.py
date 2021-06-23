# Generated by Django 3.2.3 on 2021-05-24 12:33

import _socket
from django.conf import settings
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.fields.other_charfield
import edc_model.models.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("inte_lists", "0011_auto_20210524_1533"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inte_subject", "0079_auto_20210425_0301"),
    ]

    operations = [
        migrations.CreateModel(
            name="IntegratedCareReview",
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
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
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
                ("consent_model", models.CharField(editable=False, max_length=50, null=True)),
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
                    "receive_health_talk_messages",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Do you receive health messages when attending this clinic?",
                    ),
                ),
                (
                    "health_talk_conditions_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "health_talk_focus_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "health_talk_presenters_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "additional_health_advice",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Did you receive any additional health advice during your visits?",
                    ),
                ),
                (
                    "health_advice_advisor_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "health_advice_focus_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "receive_rx_today",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Did you receive a drug prescription today?",
                    ),
                ),
                (
                    "rx_collection_hcf",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No, I buy my own drugs"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, are you collecting it from the healthcare facility?",
                    ),
                ),
                (
                    "where_rx_dispensed_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "who_dispenses_rx_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "hospital_card",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("Dont_know", "Do not know")],
                        max_length=15,
                        verbose_name="Do you have a hospital card used in the clinic?",
                    ),
                ),
                (
                    "hospital_card_type",
                    models.CharField(
                        choices=[
                            ("paper_based", "Paper-based"),
                            ("electronic", "Electronic"),
                            ("both", "Both"),
                            ("N/A", "Not Applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, what type of card is this?",
                    ),
                ),
                (
                    "missed_appt",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Have you missed an appointment since you started attending this clinic?",
                    ),
                ),
                (
                    "missed_appt_call",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, did you get a phone call from the clinic about the missed visit?",
                    ),
                ),
                (
                    "missed_appt_call_who",
                    models.CharField(
                        choices=[
                            ("nurse", "Nurse"),
                            ("OTHER", "Other"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, who called you about the missed visit?",
                    ),
                ),
                (
                    "missed_appt_call_who_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "lab_tests",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Have you done any laboratory tests since you started in this clinic?",
                    ),
                ),
                (
                    "pay_for_lab_tests",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, did you pay for any of the tests?",
                    ),
                ),
                (
                    "which_lab_tests_charged_for_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "health_advice_advisor",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_inte_subject_integratedcarereview_health_advice_advisor_+",
                        to="inte_lists.HealthAdvisors",
                        verbose_name="If YES, who gave this health advice?",
                    ),
                ),
                (
                    "health_advice_focus",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_inte_subject_integratedcarereview_health_advice_focus_+",
                        to="inte_lists.HealthInterventionTypes",
                        verbose_name="If YES, what was the focus of the advice?",
                    ),
                ),
                (
                    "health_talk_conditions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_inte_subject_integratedcarereview_health_talk_conditions_+",
                        to="inte_lists.HealthTalkConditions",
                        verbose_name="If YES, what disease conditions are discussed during health talks?",
                    ),
                ),
                (
                    "health_talk_focus",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_inte_subject_integratedcarereview_health_talk_focus_+",
                        to="inte_lists.HealthInterventionTypes",
                        verbose_name="If YES, what type of messages are delivered during health talks?",
                    ),
                ),
                (
                    "health_talk_presenters",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_inte_subject_integratedcarereview_health_talk_presenters_+",
                        to="inte_lists.HealthAdvisors",
                        verbose_name="If YES, who gives the health talks?",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.site",
                    ),
                ),
                (
                    "subject_visit",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inte_subject.subjectvisit",
                    ),
                ),
                (
                    "where_rx_dispensed",
                    models.ManyToManyField(
                        blank=True,
                        to="inte_lists.DrugDispensaries",
                        verbose_name="If YES, where in the healthcare facility are your drugs dispensed from?",
                    ),
                ),
                (
                    "which_lab_tests_charged_for",
                    models.ManyToManyField(
                        blank=True,
                        to="inte_lists.LaboratoryTests",
                        verbose_name="If YES, what tests are you charged for?",
                    ),
                ),
                (
                    "who_dispenses_rx",
                    models.ManyToManyField(
                        blank=True,
                        to="inte_lists.DrugDispensers",
                        verbose_name="If YES, who in the healthcare facility is responsible for dispensing your drugs?",
                    ),
                ),
            ],
            options={
                "verbose_name": "Integrated Care Review",
                "verbose_name_plural": "Integrated Care Reviews",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalIntegratedCareReview",
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
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
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
                ("consent_model", models.CharField(editable=False, max_length=50, null=True)),
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
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "receive_health_talk_messages",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Do you receive health messages when attending this clinic?",
                    ),
                ),
                (
                    "health_talk_conditions_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "health_talk_focus_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "health_talk_presenters_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "additional_health_advice",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Did you receive any additional health advice during your visits?",
                    ),
                ),
                (
                    "health_advice_advisor_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "health_advice_focus_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "receive_rx_today",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Did you receive a drug prescription today?",
                    ),
                ),
                (
                    "rx_collection_hcf",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No, I buy my own drugs"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, are you collecting it from the healthcare facility?",
                    ),
                ),
                (
                    "where_rx_dispensed_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "who_dispenses_rx_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "hospital_card",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("Dont_know", "Do not know")],
                        max_length=15,
                        verbose_name="Do you have a hospital card used in the clinic?",
                    ),
                ),
                (
                    "hospital_card_type",
                    models.CharField(
                        choices=[
                            ("paper_based", "Paper-based"),
                            ("electronic", "Electronic"),
                            ("both", "Both"),
                            ("N/A", "Not Applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, what type of card is this?",
                    ),
                ),
                (
                    "missed_appt",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Have you missed an appointment since you started attending this clinic?",
                    ),
                ),
                (
                    "missed_appt_call",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, did you get a phone call from the clinic about the missed visit?",
                    ),
                ),
                (
                    "missed_appt_call_who",
                    models.CharField(
                        choices=[
                            ("nurse", "Nurse"),
                            ("OTHER", "Other"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, who called you about the missed visit?",
                    ),
                ),
                (
                    "missed_appt_call_who_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
                    ),
                ),
                (
                    "lab_tests",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        max_length=15,
                        verbose_name="Have you done any laboratory tests since you started in this clinic?",
                    ),
                ),
                (
                    "pay_for_lab_tests",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("N/A", "Not applicable")],
                        default="N/A",
                        max_length=15,
                        verbose_name="If YES, did you pay for any of the tests?",
                    ),
                ),
                (
                    "which_lab_tests_charged_for_other",
                    edc_model.models.fields.other_charfield.OtherCharField(
                        blank=True,
                        max_length=35,
                        null=True,
                        verbose_name="If other, please specify ...",
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
                        to="sites.site",
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
                        to="inte_subject.subjectvisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Integrated Care Review",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddIndex(
            model_name="integratedcarereview",
            index=models.Index(
                fields=["subject_visit", "site", "id"], name="inte_subjec_subject_4fc801_idx"
            ),
        ),
    ]
