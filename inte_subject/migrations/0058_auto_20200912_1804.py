# Generated by Django 3.0.9 on 2020-09-12 15:04
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations
from django.db.models.signals import pre_save
from edc_constants.constants import NO, YES
from edc_utils import DisableSignals


def update_complications_from_baseline(apps, schema_editor):
    """Splits the complications model into baseline and followup."""
    complications_model_cls = apps.get_model("inte_subject.complicationsbaseline")
    complications_followup_model_cls = apps.get_model("inte_subject.complicationsfollowup")
    clinical_review_model_cls = apps.get_model("inte_subject.clinicalreview")
    names = [
        "stroke",
        "heart_attack",
        "renal_disease",
        "vision",
        "numbness",
        "foot_ulcers",
    ]
    for clinical_review in clinical_review_model_cls.objects.all():
        try:
            complications = complications_model_cls.objects.get(
                subject_visit=clinical_review.subject_visit
            )
        except ObjectDoesNotExist:
            clinical_review.complications = NO
        else:
            clinical_review.complications = YES

            complications_followup = complications_followup_model_cls()
            complications_followup.subject_visit = clinical_review.subject_visit
            complications_followup.created = clinical_review.created
            complications_followup.modified = clinical_review.modified
            complications_followup.user_created = clinical_review.user_created
            complications_followup.user_modified = clinical_review.user_modified
            complications_followup.hostname_created = clinical_review.hostname_created
            complications_followup.hostname_modified = clinical_review.hostname_modified
            complications_followup.device_created = clinical_review.device_created
            complications_followup.device_modified = clinical_review.device_modified
            complications_followup.consent_model = clinical_review.consent_model
            complications_followup.consent_version = clinical_review.consent_version
            complications_followup.site_id = clinical_review.site_id

            for name in names:
                setattr(complications_followup, name, getattr(complications, name))
                setattr(
                    complications_followup,
                    f"{name}_date",
                    getattr(complications, f"{name}_estimated_date"),
                )

            complications_followup.complications = complications.complications

            complications_followup.other_complications = complications.other_complications
            with DisableSignals(disabled_signals=[pre_save]):
                complications_followup.save()
                complications.delete()
        with DisableSignals(disabled_signals=[pre_save]):
            clinical_review.save()
    print("\nDone. Remember to run the INTE managment command to update metadata.")


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0057_auto_20200912_1804"),
    ]

    operations = [migrations.RunPython(update_complications_from_baseline)]
