from django.apps import AppConfig


class CommentConfig(AppConfig):
    name = 'comment'
    verbose_name = '评论'

    def ready(self):
        super(CommentConfig, self).ready()
        from . import signals