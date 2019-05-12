# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse


# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def test01(request):
    """
    实验一 首页
    """
    return render(request, 'home_application/test01.html')


def test02(request):
    """
    实验二
    """
    return render(request, 'home_application/test02.html')


def get_message(request):
    """
    收到Hello Blueking,返回Congratulation!
    """
    input_message = request.GET.get('input_message')
    if input_message == 'Hello Blueking':
        data = 'Congratulation!'
    else:
        data = '请输入正确的内容!'

    result = {'result': True, 'data': data}
    return JsonResponse(result)


def test03(request):
    """
    实验三
    """
    return render(request, 'home_application/test03.html')