# Generated by Django 4.0.6 on 2022-08-13 08:59

import apps.common.custom_validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qr_image', models.ImageField(blank=True, null=True, upload_to='qrcodes')),
                ('qr_image_pdf', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('qr_image_jpg', models.ImageField(blank=True, null=True, upload_to='jpg')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('account_name', models.CharField(max_length=150)),
                ('bank_name', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=10, validators=[apps.common.custom_validators.validate_value_type_and_length])),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
                'ordering': ('created_on',),
            },
        ),
    ]
