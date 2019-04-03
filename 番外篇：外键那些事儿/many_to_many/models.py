from django.db import models

# Create your models here.
# 作者表
class Author(models.Model):
    author_name = models.CharField(max_length=24)

    def __str__(self):
        return '<Author: {0}>'.format(self.author_name)

    __unicode__ = __str__

# 书籍表
class Book(models.Model):
    book_name = models.CharField(max_length=48)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return '<Book: {0}>'.format(self.book_name)

    __unicode__ = __str__

    # 正向（顺理成章）
    # book = Book.objects.first()
    # authors = book.authors.all()  # 获得该书所有作者

    # 反向（冥冥之中）
    # author = Author.objects.first()
    # books = author.book_set.all()  # 获得该作者所有书

    # related_name，明确关系，同ForeignKey
    # authors = models.ManyToManyField(Author, related_name='books')


    # 编辑ManyToMany字段，无需执行save()保存
    # 参考：https://docs.djangoproject.com/en/2.2/ref/models/relations/#django.db.models.fields.related.RelatedManager
    # add, remove, clear
    # book = Book.objects.first()
    # author = Author.objects.first()

    # 1、书籍新增作者
    # book.authors.add(author)

    # 2、书籍移除作者
    # book.authors.remove(author)

    # 3、作者添加书籍
    # author.book_set.add(book)

    # 4、作者移除书籍
    # author.book_set.remove(book)
    