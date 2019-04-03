from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/#module-django.db.models.fields.related
# 班级表
class SchoolClass(models.Model):
    class_name = models.CharField(max_length=12)
    class_master = models.CharField(max_length=12)

    def __str__(self):
        return '<SchoolClass: {0}>'.format(self.class_name)

    __unicode__ = __str__

# 学生表
class Student(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    # （on_delete属性说明）
    # 必填，对应关联的记录（班级），删除的时候，该记录（学生）怎么处理
    # 参考：https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.on_delete

    # 1、CASCADE, 级联删除。
    # 当班级删除记录的时候，删除对应的所有学生。确保数据完整

    # 2、PROTECT, 保护。
    # 当班级删除记录的时候，若有学生关联该班级，则不给删除班级

    # 3、SET_NULL, 设置为NULL。 
    # 当班级删除记录的时候，若有学生关联该班级，则将这些学生的班级外键字段，值设置为null。
    # school_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True)  # 需要设置null为True

    # 4、SET_DEFAULT，设置为默认值。
    # def default_class():
    #     return SchoolClass.objects.first()
    # school_class = models.ForeignKey(SchoolClass, on_delete=models.SET_DEFAULT, default=default_class)  # 需要设置default

    # 5、SET()，自定义方法，返回一个值，设置该字段的值
    # 参考：https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.SET

    # 6、DO_NOTHING，什么时候都不做。
    # 这个会破坏数据完整性，慎用。


    # （正向：顺理成章）
    # s = Student.objects.first()
    # s.school_class  # 找到关联的班级对象

    # （反向：冥冥之中）
    # c = SchoolClass.objects.first()
    # c.student_set.all()  # xxxx_set 找到被关联的对象

    # related_name，明确关系，班级通过什么属性找到学生
    # school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name='students')
    # c = SchoolClass.objects.first()
    # c.students.all()


    # 编辑该字段，直接赋值即可
    # c = SchoolClass.objects.first()
    # s = Student()
    # s.student_name = 'test'
    # s.school_class = c
    # s.save()

    
    SEX_CHOICES = (
        (0, '男'),
        (1, '女'),
    )
    student_name = models.CharField(max_length=12)
    sex = models.IntegerField(choices=SEX_CHOICES, default=0)

    def __str__(self):
        return '<Student: {0}>'.format(self.student_name)

    __unicode__ = __str__
