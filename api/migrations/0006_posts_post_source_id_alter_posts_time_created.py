# Generated by Django 4.1.5 on 2024-01-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_posts_post_source_id_posts_time_created_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_source_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time_created',
            field=models.CharField(default='', max_length=255),
        ),
    ]