# Generated by Django 4.0.3 on 2022-03-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapi', '0006_alter_company_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
