# Generated by Django 4.1.1 on 2022-09-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_install_pg_trgm"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lift",
            name="weight_category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("W45", "W45"),
                    ("W49", "W49"),
                    ("W55", "W55"),
                    ("W59", "W59"),
                    ("W64", "W64"),
                    ("W71", "W71"),
                    ("W76", "W76"),
                    ("W81", "W81"),
                    ("W40", "W40"),
                    ("W81+", "W81+"),
                    ("W87", "W87"),
                    ("W87+", "W87+"),
                    ("M55", "M55"),
                    ("M61", "M61"),
                    ("M67", "M67"),
                    ("M73", "M73"),
                    ("M81", "M81"),
                    ("M89", "M89"),
                    ("M96", "M96"),
                    ("M102", "M102"),
                    ("M49", "M49"),
                    ("M102+", "M102+"),
                    ("M109", "M109"),
                    ("M109+", "M109+"),
                    ("W44", "W44"),
                    ("W48", "W48"),
                    ("W53", "W53"),
                    ("W58", "W58"),
                    ("W63", "W63"),
                    ("W69", "W69"),
                    ("W75", "W75"),
                    ("W75+", "W75+"),
                    ("W90", "W90"),
                    ("W90+", "W90+"),
                    ("M50", "M50"),
                    ("M56", "M56"),
                    ("M62", "M62"),
                    ("M69", "M69"),
                    ("M77", "M77"),
                    ("M85", "M85"),
                    ("M94", "M94"),
                    ("M94+", "M94+"),
                    ("M105", "M105"),
                    ("M105+", "M105+"),
                ],
                max_length=5,
            ),
        ),
    ]
