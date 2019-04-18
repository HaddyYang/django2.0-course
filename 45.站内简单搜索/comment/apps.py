from django.apps import AppConfig


class CommentConfig(AppConfig):
    name = 'comment'

    def ready(self):
        super(CommentConfig, self).ready()
        from . import signals