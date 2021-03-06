# Generated by Django 4.0.3 on 2022-03-18 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capstoneapi', '0003_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('isEmployer', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='employer',
            name='user',
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='description',
            field=models.CharField(max_length=10000),
        ),
        migrations.DeleteModel(
            name='Applicant',
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
    ]
