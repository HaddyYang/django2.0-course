from django.apps import AppConfig


class LikesConfig(AppConfig):
    name = 'likes'

    def ready(self):
        super(LikesConfig, self).ready()
        from . import signals