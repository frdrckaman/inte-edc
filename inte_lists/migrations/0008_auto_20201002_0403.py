# Generated by Django 3.0.9 on 2020-10-02 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_lists", "0007_auto_20200910_1742"),
    ]

    operations = [
        migrations.CreateModel(
            name="NonAdherenceReasons",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "version",
                    models.CharField(default="1.0", editable=False, max_length=35),
                ),
            ],
            options={
                "verbose_name": "NonAdherence Reasons",
                "verbose_name_plural": "NonAdherence Reasons",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
        ),
        migrations.AddIndex(
            model_name="nonadherencereasons",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="inte_lists__id_bf3e69_idx",
            ),
        ),
    ]
