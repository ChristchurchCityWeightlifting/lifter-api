# Generated by Django 4.0.3 on 2022-03-23 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_alter_lift_cnj_first_alter_lift_cnj_first_weight_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lift",
            name="competition",
        ),
    ]