# Generated by Django 4.2.7 on 2023-12-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('post_type', models.CharField(max_length=100)),
                ('post_title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('time', models.TimeField()),
                ('img', models.ImageField(blank=True, upload_to='userimages/')),
            ],
        ),
    ]