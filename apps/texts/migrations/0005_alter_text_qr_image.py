# Generated by Django 4.0.6 on 2022-08-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0004_alter_text_qr_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='qr_image',
            field=models.ImageField(blank=True, default='dummy qr.png', null=True, upload_to='qrcodes'),
        ),
    ]