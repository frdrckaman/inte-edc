from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from edc_model import models as edc_models
from inte_lists.models import ArvDrugs
from inte_subject.models import DrugRefillHiv

from ..model_mixins import DrugSupplyModelMixin


class DrugSupplyHiv(DrugSupplyModelMixin, edc_models.BaseUuidModel):

    drug_refill = models.ForeignKey(DrugRefillHiv, on_delete=models.PROTECT)

    drug = models.ForeignKey(ArvDrugs, on_delete=models.PROTECT)

    class Meta(edc_models.BaseUuidModel.Meta):
        verbose_name = "Drug Supply: Hypertension"
        verbose_name_plural = "Drug Supply: Hypertension"
