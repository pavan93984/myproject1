# Generated by Django 4.2.7 on 2023-12-12 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0007_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='myapp1.author'),
        ),
    ]