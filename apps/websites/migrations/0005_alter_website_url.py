# Generated by Django 4.0.6 on 2022-08-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("websites", "0004_remove_website_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="website",
            name="url",
            field=models.URLField(blank=None, default="https://"),
        ),
    ]
