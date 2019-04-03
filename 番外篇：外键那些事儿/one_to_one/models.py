from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=24)

    def __str__(self):
        return '<Profile: {0}>'.format(self.nickname)

    __unicode__ = __str__

    # 基本使用方法和ForeignKey一样

    # 正向：顺理成章
    # profile = Profile.objects.first()
    # user = profile.user

    # 反向：冥冥之中，我知道你的存在
    # user = User.objects.first()
    # profile = user.profile

    # 编辑该字段，直接赋值即可
