# Generated by Django 4.2.7 on 2023-12-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0017_rename_content_comment_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
