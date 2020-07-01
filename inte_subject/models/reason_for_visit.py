from django.db import models
from edc_constants.choices import YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models
from inte_lists.models import HealthServices, ClinicServices, RefillConditions

from ..model_mixins import CrfModelMixin


class ReasonForVisit(CrfModelMixin, edc_models.BaseUuidModel):

    health_services = models.ManyToManyField(
        HealthServices,
        verbose_name="Which health service(s) is the patient here for today?",
    )

    clinic_services = models.ManyToManyField(
        ClinicServices,
        verbose_name="Why is the patient at the clinic?",
        related_name="clinic_services",
        blank=True,
    )

    clinic_services_other = edc_models.OtherCharField()

    refill_hiv = models.CharField(
        verbose_name="Is the patient refilling HIV medications?",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    refill_diabetes = models.CharField(
        verbose_name="Is the patient refilling Diabetes medications?",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    refill_hypertension = models.CharField(
        verbose_name="Is the patient refilling Hypertension medications?",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    class Meta(CrfModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        verbose_name = "Reason for Visit"
        verbose_name_plural = "Reason for Visits"
