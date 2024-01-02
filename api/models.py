from django.db import models

# Create your models here.
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_source = models.CharField(max_length=255,default="")
    post_source_id = models.CharField(max_length=255,default="")
    post_author = models.CharField(max_length=255, default="")
    post_title = models.TextField(default="")
    post_description = models.TextField(default="")
    post_original_url = models.TextField(default="")
    url_to_image = models.TextField(default="")   
    post_content = models.TextField(default="")
    post_slug = models.CharField(max_length=255,default="")
    time_created = models.CharField(max_length=255,default="")
    time_created_text = models.CharField(max_length=255,default="")
    net_views = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title
    
class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_text = models.TextField(default="")
    time_created = models.IntegerField()

    def __str__(self):
        return self.comment_text