# Generated by Django 4.0.6 on 2022-08-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0002_alter_social_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='qr_image',
            field=models.ImageField(blank=True, default='media/dummy qr.png', null=True, upload_to='qrcodes'),
        ),
    ]
