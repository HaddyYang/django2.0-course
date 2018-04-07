from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import JsonResponse
from .models import Comment
from .forms import CommentForm


def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentForm(request.POST, user=request.user)
    if comment_form.is_valid():
        # 检查通过，保存数据
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.save()

        data = {}
        data['status'] = 'SUCCESS'
        data['username'] = comment.user.username
        data['text'] = comment.text
        data['comment_time'] = comment.comment_time.strftime("%Y-%m-%d %H:%M:%S")
        return JsonResponse(data)
    else:
        data = {}
        data['status'] = 'ERROR'
        #data['message'] = comment_form.errors
        if comment_form.non_field_errors():
            data['message'] = comment_form.non_field_errors()[0]
        elif comment_form.has_error('text'):
            data['message'] = '评论内容不能为空'
        return JsonResponse(data)