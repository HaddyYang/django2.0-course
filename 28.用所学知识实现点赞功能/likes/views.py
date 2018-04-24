from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from .models import LikeCount, LikeRecord


def ErrorResponse(code, message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = message
    return JsonResponse(data)

def SuccessResponse(liked_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['liked_num'] = liked_num
    return JsonResponse(data)

def like_change(request):
    user = request.user
    if not user.is_authenticated:
        return ErrorResponse(400, 'user is not login')

    try:
        content_type = request.GET.get('content_type')
        content_type = ContentType.objects.get(model=content_type)
        
        object_id = int(request.GET.get('object_id'))
        model_class = content_type.model_class()
        model_object = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist:
        return ErrorResponse(401, 'object does not exist')    

    if request.GET.get('is_like') == 'true':
        # 点赞，添加点赞记录，点赞总数+1
        like_record, created = LikeRecord.objects.get_or_create(content_type=content_type, object_id=object_id, user=user)
        if created:
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            like_count.liked_num += 1
            like_count.save()
            return SuccessResponse(like_count.liked_num)
        else:
            # 已经点赞过了，不能再记录
            return ErrorResponse(402, 'you were liked')
    else:
        # 取消点赞，删除点赞记录，点赞总数-1
        if LikeRecord.objects.filter(content_type=content_type, object_id=object_id, user=user).exists():
            like_record = LikeRecord.objects.get(content_type=content_type, object_id=object_id, user=user)
            like_record.delete()
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            if not created:
                like_count.liked_num -= 1
                like_count.save()
                return SuccessResponse(like_count.liked_num)
            else:
                return ErrorResponse(403, 'data error')
        else:
            # 没有点赞记录，不能操作
            return ErrorResponse(404, 'you were not liked')
