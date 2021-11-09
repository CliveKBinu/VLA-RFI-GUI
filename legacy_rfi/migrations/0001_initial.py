# Generated by Django 3.2.7 on 2021-09-27 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterRfiCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.IntegerField(blank=True, null=True)),
                ('frontend', models.CharField(blank=True, max_length=15, null=True)),
                ('azimuth_deg_field', models.DecimalField(blank=True, db_column='azimuth_deg', decimal_places=5, max_digits=8, null=True)),
                ('projid', models.CharField(blank=True, max_length=50, null=True)),
                ('resolution_mhz_field', models.DecimalField(blank=True, db_column='resolution_mhz', decimal_places=10, max_digits=11, null=True)),
                ('window', models.IntegerField(blank=True, db_column='Window', null=True)),
                ('exposure', models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True)),
                ('utc_hrs', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('date', models.CharField(blank=True, max_length=10, null=True)),
                ('number_if_windows', models.IntegerField(blank=True, db_column='number_IF_Windows', null=True)),
                ('channel', models.IntegerField(blank=True, db_column='Channel', null=True)),
                ('backend', models.CharField(blank=True, max_length=12, null=True)),
                ('mjd', models.DecimalField(blank=True, decimal_places=3, max_digits=8)),
                ('frequency_mhz', models.DecimalField(blank=True, db_column='Frequency_MHz', decimal_places=4, max_digits=12)),
                ('lst', models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True)),
                ('filename', models.CharField(blank=True, max_length=100, null=True)),
                ('polarization', models.CharField(blank=True, max_length=1, null=True)),
                ('source', models.CharField(blank=True, max_length=11, null=True)),
                ('tsys', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('frequency_type', models.CharField(blank=True, max_length=4, null=True)),
                ('units', models.CharField(blank=True, max_length=2, null=True)),
                ('intensity_jy', models.DecimalField(blank=True, db_column='Intensity_Jy', decimal_places=6, max_digits=15, null=True)),
                ('scan_number', models.IntegerField(blank=True, null=True)),
                ('elevation_deg_field', models.DecimalField(blank=True, db_column='elevation_deg', decimal_places=6, max_digits=8, null=True)),
            ],
            options={
                'db_table': 'Master_RFI_Catalog',
                'managed': True,
            },
        ),
    ]
