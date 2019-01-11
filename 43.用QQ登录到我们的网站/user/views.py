import string
import random
import time
import json
from urllib.request import urlopen
from urllib.parse import urlencode, parse_qs
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import LoginForm, RegForm, ChangeNicknameForm, BindEmailForm, ChangePasswordForm, ForgotPasswordForm, BindQQForm
from .models import Profile, OAuthRelationship


def login_by_qq(request):
    code = request.GET['code']
    state = request.GET['state']

    if state != settings.QQ_STATE:
        raise Exception("state error")

    # 获取Access_token
    params = {
        'grant_type': 'authorization_code',
        'client_id': settings.QQ_APP_ID,
        'client_secret': settings.QQ_APP_KEY,
        'code': code,
        'redirect_uri': settings.QQ_REDIRECT_URL,

    }
    response = urlopen('https://graph.qq.com/oauth2.0/token?' + urlencode(params))
    data = response.read().decode('utf8')
    access_token = parse_qs(data)['access_token'][0]

    # 获取openid
    response = urlopen('https://graph.qq.com/oauth2.0/me?access_token=' + access_token)
    data = response.read().decode('utf8')
    openid = json.loads(data[10:-4])['openid']

    # 判断openid是否有关联的用户
    if OAuthRelationship.objects.filter(openid=openid, oauth_type=0).exists():
        relationship = OAuthRelationship.objects.get(openid=openid, oauth_type=0)
        auth.login(request, relationship.user)
        return redirect(reverse('home'))
    else:
        request.session['openid'] = openid

        # 获取QQ用户信息
        params = {
            'access_token': access_token,
            'oauth_consumer_key': settings.QQ_APP_ID,
            'openid': openid,
        }
        response = urlopen('https://graph.qq.com/user/get_user_info?' + urlencode(params))
        data = json.loads(response.read().decode('utf8'))
        params = {
            'nickname': data['nickname'],
            'avatar': data['figureurl_qq_1'],
        }
        return redirect(reverse('bind_qq') + '?' + urlencode(params))

def bind_qq(request):
    if request.method == 'POST':
        bind_qq_form = BindQQForm(request.POST)
        if bind_qq_form.is_valid():
            user = bind_qq_form.cleaned_data['user']
            openid = request.session.pop('openid')
            
            # 记录关系
            relationship = OAuthRelationship()
            relationship.user = user
            relationship.openid = openid
            relationship.oauth_type = 0
            relationship.save()

            # 登录
            auth.login(request, user)
            return redirect(reverse('home'))
    else:
        bind_qq_form = BindQQForm()

    context = {}
    context['bind_qq_form'] = bind_qq_form
    context['nickname'] = request.GET['nickname']
    context['avatar'] = request.GET['avatar']
    return render(request, 'user/bind_qq.html', context)

def create_user_by_qq(request):
    # 创建随机用户
    username = str(int(time.time()))
    password = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    user = User.objects.create_user(username, '', password)

    profile = Profile()
    profile.user = user
    profile.nickname = request.GET['nickname']
    profile.save()

    # 记录关系
    openid = request.session.pop('openid')
    relationship = OAuthRelationship()
    relationship.user = user
    relationship.openid = openid
    relationship.oauth_type = 0
    relationship.save()

    # 登录
    auth.login(request, user)
    return redirect(reverse('home'))

def login_for_medal(request):
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():
        user = login_form.cleaned_data['user']
        auth.login(request, user)
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'user/login.html', context)

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST, request=request)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 清除session
            del request.session['register_code']
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'user/register.html', context)
    
def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))

def user_info(request):
    context = {}
    return render(request, 'user/user_info.html', context)
    

def change_nickname(request):
    redirect_to = request.GET.get('from', reverse('home'))

    if request.method == 'POST':
        form = ChangeNicknameForm(request.POST, user=request.user)
        if form.is_valid():
            nickname_new = form.cleaned_data['nickname_new']
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.nickname = nickname_new
            profile.save()
            return redirect(redirect_to)
    else:
        form = ChangeNicknameForm()

    context = {}
    context['page_title'] = '修改昵称'
    context['form_title'] = '修改昵称'
    context['submit_text'] = '修改'
    context['form'] = form
    context['return_back_url'] = redirect_to
    return render(request, 'form.html', context)

def bind_email(request):
    redirect_to = request.GET.get('from', reverse('home'))

    if request.method == 'POST':
        form = BindEmailForm(request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.user.email = email
            request.user.save()
            # 清除session
            del request.session['bind_email_code']
            return redirect(redirect_to)
    else:
        form = BindEmailForm()

    context = {}
    context['page_title'] = '绑定邮箱'
    context['form_title'] = '绑定邮箱'
    context['submit_text'] = '绑定'
    context['form'] = form
    context['return_back_url'] = redirect_to
    return render(request, 'user/bind_email.html', context)

def send_verification_code(request):
    email = request.GET.get('email', '')
    send_for = request.GET.get('send_for', '')
    data = {}

    if email != '':
        # 生成验证码
        code = ''.join(random.sample(string.ascii_letters + string.digits, 4))
        now = int(time.time())
        send_code_time = request.session.get('send_code_time', 0)
        if now - send_code_time < 30:
            data['status'] = 'ERROR'
        else:
            request.session[send_for] = code
            request.session['send_code_time'] = now
            
            # 发送邮件
            send_mail(
                '绑定邮箱',
                '验证码：%s' % code,
                '2872402050@qq.com',
                [email],
                fail_silently=False,
            )
            data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)

def change_password(request):
    redirect_to = reverse('home')
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, user=request.user)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            auth.logout(request)
            return redirect(redirect_to)
    else:
        form = ChangePasswordForm()

    context = {}
    context['page_title'] = '修改密码'
    context['form_title'] = '修改密码'
    context['submit_text'] = '修改'
    context['form'] = form
    context['return_back_url'] = redirect_to
    return render(request, 'form.html', context)

def forgot_password(request):
    redirect_to = reverse('login')
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data['email']
            new_password = form.cleaned_data['new_password']
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            # 清除session
            del request.session['forgot_password_code']
            return redirect(redirect_to)
    else:
        form = ForgotPasswordForm()

    context = {}
    context['page_title'] = '重置密码'
    context['form_title'] = '重置密码'
    context['submit_text'] = '重置'
    context['form'] = form
    context['return_back_url'] = redirect_to
    return render(request, 'user/forgot_password.html', context)