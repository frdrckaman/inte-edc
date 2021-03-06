from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.test import TestCase, override_settings
from edc_appointment.constants import INCOMPLETE_APPT
from edc_constants.constants import (
    COMPLETE,
    FREE_OF_CHARGE,
    NO,
    NOT_APPLICABLE,
    OTHER,
    YES,
)
from edc_visit_schedule.constants import MONTH6
from model_bakery import baker
from pytz import UTC

from inte_lists.models import DrugPaySources
from inte_prn.models import IntegratedCareClinicRegistration
from inte_subject.forms import (
    HealthEconomicsRevisedForm,
    HealthEconomicsRevisedFormValidator,
)

from ..inte_test_case_mixin import InteTestCaseMixin


@override_settings(INTE_SUBJECT_HE_REVISION_DATE=datetime(2021, 4, 26, 0, 0, tzinfo=UTC))
class TestHealthEconomicsRevisionRequired(InteTestCaseMixin, TestCase):
    def setUp(self):
        super().setUp()
        now = settings.INTE_SUBJECT_HE_REVISION_DATE - relativedelta(months=6)
        self.subject_screening = self.get_subject_screening(
            report_datetime=now,
            eligibility_datetime=settings.INTE_SUBJECT_HE_REVISION_DATE
            - relativedelta(months=6),
        )
        self.subject_consent = self.get_subject_consent(
            self.subject_screening,
            consent_datetime=now,
        )
        self.subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            appt_datetime=now,
        )
        baker.make(
            "inte_subject.clinicalreviewbaseline",
            subject_visit=self.subject_visit,
            hiv_dx=YES,
        )
        baker.make(
            "hivinitialreview",
            subject_visit=self.subject_visit,
        )

    def test_he_rev_one_required_at_6m_by_date(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=MONTH6,
            appt_datetime=settings.INTE_SUBJECT_HE_REVISION_DATE - relativedelta(days=10),
        )

        crfs = self.get_crf_metadata(subject_visit)

        self.assertIn("inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()])
        self.assertNotIn(
            "inte_subject.healtheconomicsrevisedtwo", [o.model for o in crfs.all()]
        )

    def test_he_rev_two_required_at_6m_by_date(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=MONTH6,
            appt_datetime=settings.INTE_SUBJECT_HE_REVISION_DATE + relativedelta(days=10),
        )

        crfs = self.get_crf_metadata(subject_visit)

        self.assertNotIn("inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()])
        self.assertIn("inte_subject.healtheconomicsrevisedtwo", [o.model for o in crfs.all()])

    def test_not_required_6m_visit_if_he_rev_one_completed_previously(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=MONTH6,
            appt_datetime=settings.INTE_SUBJECT_HE_REVISION_DATE - relativedelta(days=10),
        )

        baker.make(
            "inte_subject.healtheconomicsrevised",
            subject_visit=subject_visit,
            report_datetime=subject_visit.report_datetime,
        )

        crfs = self.get_crf_metadata(subject_visit)

        self.assertNotIn("inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()])
        self.assertNotIn(
            "inte_subject.healtheconomicsrevisedtwo", [o.model for o in crfs.all()]
        )

    def test_not_required_6m_visit_if_he_rev_two_completed_previously(self):
        self.subject_visit.appointment.appt_status = INCOMPLETE_APPT
        self.subject_visit.appointment.save()
        self.subject_visit.appointment.refresh_from_db()

        subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
            visit_code=MONTH6,
            appt_datetime=settings.INTE_SUBJECT_HE_REVISION_DATE + relativedelta(days=10),
        )

        baker.make(
            "inte_subject.healtheconomicsrevisedtwo",
            subject_visit=subject_visit,
            report_datetime=subject_visit.report_datetime,
        )

        crfs = self.get_crf_metadata(subject_visit)

        self.assertNotIn("inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()])
        self.assertNotIn(
            "inte_subject.healtheconomicsrevisedtwo", [o.model for o in crfs.all()]
        )


class TestHealthEconomicsRevisedFormValidator(InteTestCaseMixin, TestCase):

    sid_count_for_tests = 1
    form_validator_default_form_cls = HealthEconomicsRevisedFormValidator

    def setUp(self):
        super().setUp()
        self.subject_screening = self.get_subject_screening()
        self.subject_consent = self.get_subject_consent(self.subject_screening)
        self.subject_visit = self.get_subject_visit(
            subject_screening=self.subject_screening,
            subject_consent=self.subject_consent,
        )
        baker.make(
            "inte_subject.clinicalreviewbaseline",
            subject_visit=self.subject_visit,
            hiv_dx=YES,
        )
        baker.make(
            "hivinitialreview",
            subject_visit=self.subject_visit,
        )

    @override_settings(SITE_ID=103)
    def test_form_validator_requires_icc_registration_for_intervention(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "crf_status": COMPLETE,
            "report_datetime": self.subject_visit.report_datetime,
        }
        form = HealthEconomicsRevisedForm(data=cleaned_data)
        form.is_valid()
        self.assertIn("__all__", form._errors)
        self.assertIn(
            IntegratedCareClinicRegistration._meta.verbose_name,
            ";".join(form._errors.get("__all__")),
        )

    @override_settings(SITE_ID=101)
    def test_form_validator_does_not_require_icc_registration_for_control(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "crf_status": COMPLETE,
            "report_datetime": self.subject_visit.report_datetime,
        }
        form = HealthEconomicsRevisedForm(data=cleaned_data)
        form.is_valid()
        self.assertNotIn(
            IntegratedCareClinicRegistration._meta.verbose_name,
            ";".join(form._errors.get("__all__") or []),
        )

    def test_form_validator_education(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "crf_status": COMPLETE,
            "report_datetime": self.subject_visit.report_datetime,
        }

        cleaned_data.update({"education_in_years": None, "education_certificate": None})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("education_certificate", form_validator._errors)

        cleaned_data.update({"education_in_years": 0, "education_certificate": None})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("education_certificate", form_validator._errors)

        cleaned_data.update({"education_in_years": 0, "education_certificate": "blah"})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("education_certificate", form_validator._errors)

        cleaned_data.update({"education_in_years": 1, "education_certificate": None})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("education_certificate", form_validator._errors)

        cleaned_data.update({"education_in_years": 1, "education_certificate": "blah"})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("education_certificate", form_validator._errors)

        # years of education exceeds age
        cleaned_data.update({"education_in_years": 100, "education_certificate": None})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("education_in_years", form_validator._errors)

    def test_form_validator_income(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": NO,
            "highest_earner": None,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("highest_earner", form_validator._errors)

    @override_settings(SITE_ID=103)
    def test_form_validator_expenditure(self):
        baker.make("inte_prn.integratedcareclinicregistration")
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

    def test_form_validator_requires_dx(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_month": YES,
            "rx_dm_month": YES,
        }
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_dm_month", form_validator._errors)
        self.assertIn(
            "Patient was not previously diagnosed with diabetes",
            str(form_validator._errors.get("rx_dm_month")),
        )

        cleaned_data.update({"rx_dm_month": NOT_APPLICABLE})
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("rx_dm_month", form_validator._errors)
        self.assertDictEqual({}, form_validator._errors)

    def test_form_validator_recv_drugs_month(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_month": YES,
        }

        # is an HIV patient, applicable
        cleaned_data.update(rx_hiv_month=NOT_APPLICABLE)
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_hiv_month", form_validator._errors)

        # rx_hiv_paid_month is required
        cleaned_data.update(rx_hiv_month=YES)
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_hiv_paid_month", form_validator._errors)

        cleaned_data.update(rx_hiv_month=YES, rx_hiv_paid_month=[])
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_hiv_paid_month", form_validator._errors)

        # check if "free of charge" then enforces a single selection
        cleaned_data.update(rx_hiv_month=YES, rx_hiv_paid_month=DrugPaySources.objects.all())
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_hiv_paid_month", form_validator._errors)

        # check if not "free of charge" then requires cost
        cleaned_data.update(
            rx_hiv_month=YES,
            rx_hiv_paid_month=DrugPaySources.objects.exclude(name__in=[FREE_OF_CHARGE, OTHER]),
        )
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_hiv_cost_month", form_validator._errors)

        # check if not "free of charge" then requires cost
        cleaned_data.update(
            rx_hiv_month=YES,
            rx_hiv_paid_month=DrugPaySources.objects.exclude(name__in=[FREE_OF_CHARGE, OTHER]),
            rx_hiv_cost_month=1000,
        )
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("rx_hiv_paid_month", form_validator._errors)
        self.assertNotIn("rx_hiv_cost_month", form_validator._errors)
        self.assertNotIn("rx_hiv_paid_month_other", form_validator._errors)

        # check other
        cleaned_data.update(
            rx_hiv_month=YES,
            rx_hiv_paid_month=DrugPaySources.objects.filter(name=OTHER),
            rx_hiv_cost_month=1000,
        )
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_hiv_paid_month_other", form_validator._errors)

    def test_form_validator_recv_drugs_all_no(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_today": NO,
            "rx_dm_today": NOT_APPLICABLE,
            "rx_htn_today": NOT_APPLICABLE,
            "rx_hiv_today": NOT_APPLICABLE,
            "rx_other_today": NOT_APPLICABLE,
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("rx_dm_today", form_validator._errors)
        self.assertNotIn("rx_htn_today", form_validator._errors)
        self.assertNotIn("rx_hiv_today", form_validator._errors)

    def test_form_validator_recv_drugs_yes_hiv_applicable(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_today": YES,
            "rx_dm_today": NOT_APPLICABLE,
            "rx_htn_today": NOT_APPLICABLE,
            "rx_hiv_today": NOT_APPLICABLE,
            "rx_other_today": NOT_APPLICABLE,
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_hiv_today", form_validator._errors)
        self.assertNotIn("rx_dm_today", form_validator._errors)
        self.assertNotIn("rx_htn_today", form_validator._errors)

    def test_form_validator_recv_drugs_yes_dm_yes(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_today": YES,
            "rx_dm_today": YES,
            "rx_htn_today": NOT_APPLICABLE,
            "rx_hiv_today": NO,
            "rx_other_today": NOT_APPLICABLE,
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_dm_today", form_validator._errors)
        self.assertNotIn("rx_htn_today", form_validator._errors)
        self.assertNotIn("rx_hiv_today", form_validator._errors)

    def test_form_validator_recv_drugs_yes_other_na_raises(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_today": YES,
            "rx_dm_today": NOT_APPLICABLE,
            "rx_htn_today": NOT_APPLICABLE,
            "rx_hiv_today": NO,
            "rx_other_today": NOT_APPLICABLE,
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_other_today", form_validator._errors)
        self.assertNotIn("rx_htn_today", form_validator._errors)
        self.assertNotIn("rx_hiv_today", form_validator._errors)
        self.assertNotIn("rx_dm_today", form_validator._errors)

    def test_form_validator_recv_drugs_yes_other_no(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_today": YES,
            "rx_dm_today": NOT_APPLICABLE,
            "rx_htn_today": NOT_APPLICABLE,
            "rx_hiv_today": NO,
            "rx_other_today": NO,
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertNotIn("rx_other_today", form_validator._errors)
        self.assertNotIn("rx_htn_today", form_validator._errors)
        self.assertNotIn("rx_hiv_today", form_validator._errors)
        self.assertNotIn("rx_dm_today", form_validator._errors)

    def test_form_validator_non_drug_activities(self):
        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_month": NO,
            "rx_dm_month": NOT_APPLICABLE,
            "rx_htn_month": NOT_APPLICABLE,
            "rx_hiv_month": NOT_APPLICABLE,
            "rx_other_month": NOT_APPLICABLE,
            "received_rx_today": NO,
            "rx_dm_today": NOT_APPLICABLE,
            "rx_htn_today": NOT_APPLICABLE,
            "rx_hiv_today": NOT_APPLICABLE,
            "rx_other_today": NOT_APPLICABLE,
        }

        cleaned_data.update(
            {
                "non_drug_activities_month": YES,
                "non_drug_activities_detail_month": None,
                "non_drug_activities_cost_month": None,
            }
        )
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("non_drug_activities_detail_month", form_validator._errors)

        cleaned_data.update(
            {
                "non_drug_activities_month": YES,
                "non_drug_activities_detail_month": "blah",
                "non_drug_activities_cost_month": None,
            }
        )
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("non_drug_activities_cost_month", form_validator._errors)

        cleaned_data.update(
            {
                "non_drug_activities_month": YES,
                "non_drug_activities_detail_month": "blah",
                "non_drug_activities_cost_month": 10,
            }
        )
        form_validator = self.validate_form_validator(cleaned_data)
        self.assertDictEqual({}, form_validator._errors)

    def test_not_required_at_baseline(self):
        crfs = self.get_crf_metadata(self.subject_visit)
        self.assertNotIn("inte_subject.healtheconomics", [o.model for o in crfs.all()])
        self.assertNotIn("inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()])
        self.assertNotIn(
            "inte_subject.healtheconomicsrevisedtwo", [o.model for o in crfs.all()]
        )
        self.subject_visit.save()

        crfs = self.get_crf_metadata(self.subject_visit)
        self.assertNotIn("inte_subject.healtheconomics", [o.model for o in crfs.all()])
        self.assertNotIn("inte_subject.healtheconomicsrevised", [o.model for o in crfs.all()])
        self.assertNotIn(
            "inte_subject.healtheconomicsrevisedtwo", [o.model for o in crfs.all()]
        )

    def test_rx_against_diagnosis(self):

        cleaned_data = {
            "subject_visit": self.subject_visit,
            "report_datetime": self.subject_visit.report_datetime,
            "crf_status": COMPLETE,
            "education_in_years": 10,
            "education_certificate": "secondary",
            "is_highest_earner": YES,
            "food_per_month": None,
            "accomodation_per_month": None,
            "large_expenditure_year": None,
            "received_rx_month": NO,
            "rx_dm_month": NOT_APPLICABLE,
            "rx_htn_month": NOT_APPLICABLE,
            "rx_hiv_month": NOT_APPLICABLE,
            "rx_other_month": NOT_APPLICABLE,
            "received_rx_today": YES,
            "rx_dm_today": YES,
            "rx_htn_today": NOT_APPLICABLE,
            "rx_hiv_today": NO,
            "rx_other_today": NO,
            "non_drug_activities_month": YES,
            "non_drug_activities_detail_month": "blah",
            "non_drug_activities_cost_month": 10,
        }

        form_validator = self.validate_form_validator(cleaned_data)
        self.assertIn("rx_dm_today", form_validator._errors)
        self.assertNotIn("rx_hiv_today", form_validator._errors)
