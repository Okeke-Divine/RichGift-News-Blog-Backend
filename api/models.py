from django.db import models

# Create your models here.
class Posts(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_title = models.TextField()
    post_content = models.TextField()
    post_slug = models.CharField(max_length=255)
    time_created = models.IntegerField()
    net_views = models.IntegerField(default=0)

    def __str__(self):
        return self.none
    
class Comments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    post_id = models.IntegerField()
    comment_text = models.TextField()
    time_created = models.IntegerField()

    def __str__(self):
        return self.none