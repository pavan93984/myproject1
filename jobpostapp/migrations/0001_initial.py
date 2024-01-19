# Generated by Django 4.2.7 on 2024-01-18 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titel', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=400)),
                ('company', models.CharField(max_length=100)),
                ('postes_on', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('Roles', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_no', models.BigIntegerField()),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='jobpostapp.jobpost')),
            ],
        ),
    ]
