# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from home_application.models import HostRecord


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


def save_record(request):
    """
    保存主机记录
    """
    host_ip = request.POST.get('host_ip', '')
    host_os = request.POST.get('host_os', '')
    host_partition = request.POST.get('host_partition', '')

    data = {
        'host_ip': host_ip,
        'host_os': host_os,
        'host_partition': host_partition,
        'operator': request.user.username,
    }
    result = HostRecord.objects.save_record(data)
    return JsonResponse(result)


def get_records(request):
    """
    查询主机记录
    """
    record_list = HostRecord.objects.all().order_by('-id')
    data = []
    for index, record in enumerate(record_list):
        data.append({
            'index': index,
            'host_ip': record.host_ip,
            'host_os': record.host_os,
            'host_partition': record.host_partition,
            'record_time': record.record_time,
            'operator': record.operator,
        })
    return JsonResponse({'code': 0, 'data': data})

