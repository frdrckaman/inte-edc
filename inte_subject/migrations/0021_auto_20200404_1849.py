# Generated by Django 3.0.4 on 2020-04-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_subject", "0020_auto_20200404_1819"),
    ]

    operations = [
        migrations.AddField(
            model_name="diabetesinitialreview",
            name="fasted",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AddField(
            model_name="diabetesinitialreview",
            name="glucose",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Glucose <u>level</u>",
            ),
        ),
        migrations.AddField(
            model_name="diabetesinitialreview",
            name="glucose_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="<u>Time</u> glucose <u>level</u> measured",
            ),
        ),
        migrations.AddField(
            model_name="diabetesinitialreview",
            name="glucose_quantifier",
            field=models.CharField(
                choices=[
                    ("=", "="),
                    (">", ">"),
                    (">=", ">="),
                    ("<", "<"),
                    ("<=", "<="),
                ],
                default="=",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="diabetesinitialreview",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (glucose)",
            ),
        ),
        migrations.AddField(
            model_name="historicaldiabetesinitialreview",
            name="fasted",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                max_length=15,
                null=True,
                verbose_name="Has the participant fasted?",
            ),
        ),
        migrations.AddField(
            model_name="historicaldiabetesinitialreview",
            name="glucose",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Glucose <u>level</u>",
            ),
        ),
        migrations.AddField(
            model_name="historicaldiabetesinitialreview",
            name="glucose_datetime",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="<u>Time</u> glucose <u>level</u> measured",
            ),
        ),
        migrations.AddField(
            model_name="historicaldiabetesinitialreview",
            name="glucose_quantifier",
            field=models.CharField(
                choices=[
                    ("=", "="),
                    (">", ">"),
                    (">=", ">="),
                    ("<", "<"),
                    ("<=", "<="),
                ],
                default="=",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="historicaldiabetesinitialreview",
            name="glucose_units",
            field=models.CharField(
                blank=True,
                choices=[("mg/dL", "mg/dL"), ("mmol/L", "mmol/L")],
                max_length=15,
                null=True,
                verbose_name="Units (glucose)",
            ),
        ),
    ]