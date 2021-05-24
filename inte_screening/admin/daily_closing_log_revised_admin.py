from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple

from inte_screening.models.daily_closing_log_revised import get_daily_log_revision_date

from ..admin_site import inte_screening_admin
from ..forms import DailyClosingLogRevisedForm
from ..models import DailyClosingLogRevised
from .daily_closing_log_admin import DailyClosingLogAdmin


@admin.register(DailyClosingLogRevised, site=inte_screening_admin)
class DailyClosingLogRevisedAdmin(DailyClosingLogAdmin):
    form = DailyClosingLogRevisedForm

    fieldsets = (
        [None, {"fields": ("log_date", "site")}],
        [
            "Daily Closing Log",
            {
                "fields": (
                    "clinic_services",
                    "clinic_start_time",
                    "attended",
                    "clinic_end_time",
                    "comment",
                )
            },
        ],
        audit_fieldset_tuple,
    )

    list_display = (
        "log_date",
        "clinic_services",
        "number_attended",
        "clinic_start_time",
        "clinic_end_time",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(log_date__gte=get_daily_log_revision_date())
