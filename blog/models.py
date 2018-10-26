from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogArticles(models.Model):
    title=models.CharField(max_length=300)
    #规定了字段title的属性为CharField（）类型，并且以参数max_length=30的形式说明宇段的最大数量。
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    #②通过字段author规定了博客文章和用户之间的关系一一一个用户对应多篇文章，F oreignKey（）就反映了这种“一对多”关系。类User就 是BlogA口icles的对应对象，related_ name＝”blog_posts”的作用是允许通过类User反向 查询到BlogArticles.

    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=("-publish",)

    def __str__(self):
        return self.title