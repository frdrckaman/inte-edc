# Generated by Django 3.0.6 on 2020-07-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_screening", "0005_auto_20200702_2155"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubjectrefusal",
            name="comment",
            field=models.TextField(blank=True, null=True, verbose_name="Additional Comments"),
        ),
        migrations.AddField(
            model_name="subjectrefusal",
            name="comment",
            field=models.TextField(blank=True, null=True, verbose_name="Additional Comments"),
        ),
    ]
