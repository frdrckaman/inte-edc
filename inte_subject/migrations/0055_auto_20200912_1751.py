# Generated by Django 3.0.9 on 2020-09-12 14:51

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
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("inte_lists", "0007_auto_20200910_1742"),
        ("sites", "0002_alter_domain_unique"),
        ("inte_subject", "0054_auto_20200912_1746"),
    ]

    operations = [
        migrations.RenameModel(
            new_name="ComplicationsBaseline",
            old_name="Complications",
        ),
        migrations.RenameModel(
            new_name="HistoricalComplicationsBaseline",
            old_name="HistoricalComplications",
        ),
    ]
