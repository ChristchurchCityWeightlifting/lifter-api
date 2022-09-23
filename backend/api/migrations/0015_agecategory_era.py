# Generated by Django 4.1.1 on 2022-09-22 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_agecategoryera_remove_agecategory_era_delete_era"),
    ]

    operations = [
        migrations.AddField(
            model_name="agecategory",
            name="era",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.agecategoryera",
            ),
        ),
    ]
