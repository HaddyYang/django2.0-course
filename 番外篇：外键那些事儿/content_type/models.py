from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.
# 文章表
class Article(models.Model):
    title = models.CharField(max_length=36)
    content = models.TextField(blank=True)
    # comments = GenericRelation('Comment')  # 由于Comment后面才定义，所以用字符串惰性引用

    def __str__(self):
        return '<Article: {0}>'.format(self.title)

    __unicode__ = __str__

# 视频表
class Video(models.Model):
    video_name = models.CharField(max_length=36)
    url = models.URLField()

    def __str__(self):
        return '<Video: {0}>'.format(self.video_name)

    __unicode__ = __str__

# 评论表
class Comment(models.Model):
    # 无法同时指向多个对象
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # video = models.ForeignKey(Video, on_delete=models.CASCADE)

    # 万能关系
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # 记录关联对象的类型
    object_id = models.PositiveIntegerField()  # 记录关联对象的主键值
    content_object = GenericForeignKey('content_type', 'object_id')  # 常规字段，便于使用

    # 评论内容
    text = models.TextField()

    def __str__(self):
        return '<Comment: {0}>'.format(self.text)

    __unicode__ = __str__

    # 正向，使用content_object可直接访问
    '''
    comment = Comment.objects.first()
    obj = comment.content_object  # 直接得到所被评论的对象
    '''

    # 反向，无法直接从其他对象找到Comment对应的评论
    '''
    from django.contrib.contenttypes.models import ContentType

    article = Article.objects.first()
    article_content_type = ContentType.objects.get_for_model(article)

    # 通过Comment自身的筛选查询得到
    comments = Comment.objects.filter(content_type=article_content_type, object_id=article.pk)
    '''

    # 反向，方法2，主动建立关系
    # 参考：https://docs.djangoproject.com/en/2.2/ref/contrib/contenttypes/#reverse-generic-relations
    '''
    from django.contrib.contenttypes.fields import GenericRelation
    # 对应模型加入 comments = GenericRelation('Comment') 字段

    article = Article.objects.first()
    comments = article.comments.all()
    '''


# content type 官方文档
# https://docs.djangoproject.com/en/2.2/ref/contrib/contenttypes/

# 更多可以参考，我的Django2.0教程，第22课 评论功能设计和用户登录
# 链接：https://www.bilibili.com/video/av21029850