from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, default="")
    user_fname = models.CharField(max_length=50, default="")
    user_lname = models.CharField(max_length=50, default="")
    user_profile_image_url = models.TextField(default="")

    def __str__(self):
        return self.user_name


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_source = models.CharField(max_length=255, null=True)
    post_source_id = models.CharField(max_length=255, null=True)
    post_author = models.CharField(max_length=255, default="")
    post_title = models.TextField(default="")
    post_description = models.TextField(default="")
    post_original_url = models.TextField(default="")
    url_to_image = models.TextField(default="")
    post_content = models.TextField(default="")
    post_slug = models.CharField(max_length=255, default="")
    time_created = models.DateTimeField()
    time_created_text = models.CharField(max_length=255, default="")
    net_views = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE,default="0")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default="0")
    comment_text = models.TextField(default="")
    time_created = models.DateTimeField()

    def __str__(self):
        return self.comment_text
