# Generated by Django 4.1.5 on 2024-01-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_posts_post_author_posts_post_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_source',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_source_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]
