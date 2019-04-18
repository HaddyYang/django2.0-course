import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import strip_tags
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from notifications.signals import notify
from .models import Comment


@receiver(post_save, sender=Comment)
def send_notification(sender, instance, **kwargs):
    # 发送站内消息
    if instance.reply_to is None:
        # 评论
        recipient = instance.content_object.get_user()
        if instance.content_type.model == 'blog':
            blog = instance.content_object
            verb = '{0} 评论了你的《{1}》'.format(instance.user.get_nickname_or_username(), blog.title)
        else:
            raise Exception('unkown comment object type')
    else:
        # 回复
        recipient = instance.reply_to
        verb = '{0} 回复了你的评论“{1}”'.format(
                instance.user.get_nickname_or_username(), 
                strip_tags(instance.parent.text)
            )
    url = instance.content_object.get_url() + "#comment_" + str(instance.pk)
    notify.send(instance.user, recipient=recipient, verb=verb, action_object=instance, url=url)

class SendMail(threading.Thread):
    def __init__(self, subject, text, email, fail_silently=False):
        self.subject = subject
        self.text = text
        self.email = email
        self.fail_silently = fail_silently
        threading.Thread.__init__(self)

    def run(self):
        send_mail(
            self.subject, 
            '', 
            settings.EMAIL_HOST_USER, 
            [self.email], 
            fail_silently=self.fail_silently,
            html_message=self.text
        )

@receiver(post_save, sender=Comment)
def send_email(sender, instance, **kwargs):
    # 发送邮件通知
    if instance.parent is None:
        # 评论我的博客
        subject = '有人评论你的博客'
        email = instance.content_object.get_email()
    else:
        # 回复评论
        subject = '有人回复你的评论'
        email = instance.reply_to.email
    if email != '':
        context = {}
        context['comment_text'] = instance.text
        context['url'] = instance.content_object.get_url()
        text = render(None, 'comment/send_mail.html', context).content.decode('utf-8')
        send_mail = SendMail(subject, text, email)
        send_mail.start()
        