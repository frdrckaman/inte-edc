# Generated by Django 3.0.9 on 2020-09-21 13:48
from django.db import migrations
from django.db.models.signals import pre_save
from edc_constants.constants import STUDY_DEFINED_TIMEPOINT
from edc_utils import DisableSignals


def update_subjectvisit(apps, schema_editor):
    """Adds or removes selection on subject visit clinic services
    according to study timepoint.

    * Adds STUDY_DEFINED_TIMEPOINT if scheduled timepoint (XXXX.0)
    * Removes if not a scheduled timepoint (XXXX.1+)
    """
    subject_visit_model_cls = apps.get_model("inte_subject.subjectvisit")
    clinical_services_model_cls = apps.get_model("inte_lists.clinicservices")
    study_defined_timepoint = clinical_services_model_cls.objects.get(
        name=STUDY_DEFINED_TIMEPOINT
    )
    for subject_visit in subject_visit_model_cls.objects.all():
        if (
            subject_visit.visit_code_sequence == 0
            and not subject_visit.clinic_services.filter(name=STUDY_DEFINED_TIMEPOINT).exists()
        ):
            subject_visit.clinic_services.add(study_defined_timepoint)
        elif (
            subject_visit.visit_code_sequence != 0
            and subject_visit.clinic_services.filter(name=STUDY_DEFINED_TIMEPOINT).exists()
        ):
            subject_visit.clinic_services.remove(study_defined_timepoint)
        with DisableSignals(disabled_signals=[pre_save]):
            subject_visit.save()


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0002_auto_20200625_0329"),
        ("inte_subject", "0061_auto_20200915_1615"),
    ]

    operations = [migrations.RunPython(update_subjectvisit)]
