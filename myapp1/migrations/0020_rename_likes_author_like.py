# Generated by Django 4.2.7 on 2024-01-01 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0019_author_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='likes',
            new_name='like',
        ),
    ]