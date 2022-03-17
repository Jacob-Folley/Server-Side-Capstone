# Generated by Django 4.0.3 on 2022-03-15 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant_Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAccepted', models.BooleanField(default=False)),
                ('isRejected', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAccepted', models.BooleanField(default=False)),
                ('isRejected', models.BooleanField(default=False)),
                ('applicantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneapi.applied')),
                ('employerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneapi.job_posting')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.CharField(max_length=50)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(related_name='resume', through='capstoneapi.Applicant_Skills', to='capstoneapi.skills')),
            ],
        ),
        migrations.CreateModel(
            name='Posting_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneapi.job_posting')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneapi.skills')),
            ],
        ),
        migrations.AddField(
            model_name='job_posting',
            name='skills',
            field=models.ManyToManyField(related_name='postings', through='capstoneapi.Posting_Skill', to='capstoneapi.skills'),
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='applied',
            name='posting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneapi.job_posting'),
        ),
        migrations.AddField(
            model_name='applicant_skills',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneapi.resume'),
        ),
        migrations.AddField(
            model_name='applicant_skills',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstoneapi.skills'),
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]