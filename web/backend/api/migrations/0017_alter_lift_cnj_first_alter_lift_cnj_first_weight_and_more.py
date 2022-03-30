# Generated by Django 4.0.3 on 2022-03-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_alter_lift_weight_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lift",
            name="cnj_first",
            field=models.CharField(
                blank=True,
                choices=[
                    ("LIFT", "Good Lift"),
                    ("NOLIFT", "No Lift"),
                    ("DNA", "Did not attempt"),
                ],
                default="DNA",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="lift",
            name="cnj_first_weight",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="lift",
            name="cnj_second",
            field=models.CharField(
                blank=True,
                choices=[
                    ("LIFT", "Good Lift"),
                    ("NOLIFT", "No Lift"),
                    ("DNA", "Did not attempt"),
                ],
                default="DNA",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="lift",
            name="cnj_second_weight",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="lift",
            name="cnj_third",
            field=models.CharField(
                blank=True,
                choices=[
                    ("LIFT", "Good Lift"),
                    ("NOLIFT", "No Lift"),
                    ("DNA", "Did not attempt"),
                ],
                default="DNA",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="lift",
            name="cnj_third_weight",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="lift",
            name="snatch_first",
            field=models.CharField(
                blank=True,
                choices=[
                    ("LIFT", "Good Lift"),
                    ("NOLIFT", "No Lift"),
                    ("DNA", "Did not attempt"),
                ],
                default="DNA",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="lift",
            name="snatch_first_weight",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="lift",
            name="snatch_second",
            field=models.CharField(
                blank=True,
                choices=[
                    ("LIFT", "Good Lift"),
                    ("NOLIFT", "No Lift"),
                    ("DNA", "Did not attempt"),
                ],
                default="DNA",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="lift",
            name="snatch_second_weight",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="lift",
            name="snatch_third",
            field=models.CharField(
                blank=True,
                choices=[
                    ("LIFT", "Good Lift"),
                    ("NOLIFT", "No Lift"),
                    ("DNA", "Did not attempt"),
                ],
                default="DNA",
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="lift",
            name="snatch_third_weight",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="lift",
            name="team",
            field=models.CharField(blank=True, default="IND", max_length=4),
        ),
    ]
