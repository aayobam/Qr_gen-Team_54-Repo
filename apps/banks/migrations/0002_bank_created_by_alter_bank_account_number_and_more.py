# Generated by Django 4.0.6 on 2022-08-03 18:39

import apps.common.custom_validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("banks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bank",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="bank",
            name="account_number",
            field=models.CharField(
                max_length=10,
                validators=[
                    apps.common.custom_validators.validate_value_type_and_length
                ],
            ),
        ),
        migrations.AlterField(
            model_name="bank",
            name="qr_image",
            field=models.ImageField(blank=True, null=True, upload_to="qrcodes"),
        ),
    ]
