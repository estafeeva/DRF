# Generated by Django 5.0.7 on 2024-12-07 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_rename_link_payments_payment_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="payment_date",
            field=models.DateField(
                default=datetime.date(2024, 12, 7), verbose_name="дата оплаты"
            ),
        ),
    ]
