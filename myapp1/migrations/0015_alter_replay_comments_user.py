# Generated by Django 4.2.7 on 2023-12-20 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0014_remove_comment_praint_replay_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replay_comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='myapp1.comment'),
        ),
    ]
