# Generated by Django 3.2.7 on 2021-12-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rfi", "0002_scan_datetime"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="path",
            field=models.TextField(db_index=True, default="", unique=True),
            preserve_default=False,
        ),
    ]