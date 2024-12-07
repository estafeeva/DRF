# Generated by Django 5.0.7 on 2024-12-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payments"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="link",
            field=models.URLField(
                blank=True,
                help_text="Укажите ссылку на оплату",
                max_length=400,
                null=True,
                verbose_name="ссылка на оплату",
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите ID сессии",
                max_length=250,
                null=True,
                verbose_name="ID сессии",
            ),
        ),
    ]
