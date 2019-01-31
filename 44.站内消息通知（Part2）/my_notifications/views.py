from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from notifications.models import Notification


def my_notifications(request):
    context = {}
    return render(request, 'my_notifications/my_notifications.html', context)
    
def my_notification(request, my_notification_pk):
    my_notification = get_object_or_404(Notification, pk=my_notification_pk)
    my_notification.unread = False
    my_notification.save()
    return redirect(my_notification.data['url'])

def delete_my_read_notifications(request):
    notifications = request.user.notifications.read()
    notifications.delete()
    return redirect(reverse('my_notifications'))
    