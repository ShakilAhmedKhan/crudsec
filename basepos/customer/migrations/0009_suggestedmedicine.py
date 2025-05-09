# Generated by Django 5.2 on 2025-05-09 04:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0008_sale_total_amount"),
    ]

    operations = [
        migrations.CreateModel(
            name="SuggestedMedicine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.FloatField()),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.medicine",
                    ),
                ),
            ],
            options={
                "ordering": ["-score"],
                "unique_together": {("customer", "medicine", "created_at")},
            },
        ),
    ]
