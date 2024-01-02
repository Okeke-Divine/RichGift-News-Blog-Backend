# Generated by Django 4.1.5 on 2024-01-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_posts_post_source_posts_post_source_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_source_id',
        ),
        migrations.AddField(
            model_name='posts',
            name='time_created_text',
            field=models.CharField(default='', max_length=255),
        ),
    ]