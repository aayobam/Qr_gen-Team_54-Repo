# Generated by Django 4.0.6 on 2022-08-15 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contacts_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='url',
        ),
    ]
