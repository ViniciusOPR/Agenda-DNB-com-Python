# Generated by Django 4.2.7 on 2023-11-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_first_name_contact_aka_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='contact',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
