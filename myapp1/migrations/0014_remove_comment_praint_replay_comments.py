# Generated by Django 4.2.7 on 2023-12-20 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0013_remove_comment_replay_comment_praint_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='praint',
        ),
        migrations.CreateModel(
            name='replay_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='myapp1.comment')),
            ],
        ),
    ]
