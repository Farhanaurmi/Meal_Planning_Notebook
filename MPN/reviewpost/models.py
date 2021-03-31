from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Reviewpost(models.Model):
    sno=models.AutoField(primary_key=True)
    content_name = models.CharField(max_length=150, null=True)
    content = models.TextField()
    photos = models.ImageField(default="p1.png",upload_to="images/%y",null=True, blank=True)
    date_created = models.DateTimeField(default=now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='postlikes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.content_name

class ReviewComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Reviewpost,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
    date_created = models.DateTimeField(default=now)

    

	