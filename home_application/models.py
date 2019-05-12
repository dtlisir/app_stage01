# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class HostRecordManager(models.Manager):

    def save_record(self, data):
        """
        保存主机记录
        """
        try:
            HostRecord.objects.create(
                host_ip=data.get('host_ip'),
                host_os=data.get('host_os'),
                host_partition=data.get('host_partition'),
                operator=data.get('operator'),
            )
            result = {'result': True, 'message': u"保存成功"}
        except Exception as e:
            result = {'result': False, 'message': u"保存失败, %s" % e}
        return result


class HostRecord(models.Model):
    """
    主机记录
    """
    host_ip = models.CharField(u"主机IP", max_length=32)
    host_os = models.CharField(u"主机系统", max_length=64)
    host_partition = models.CharField(u"磁盘分区", max_length=64)
    record_time = models.DateTimeField(u"录入时间", default=timezone.now)
    operator = models.CharField(u"记录人", max_length=64)
    objects = HostRecordManager()

    def __unicode__(self):
        return self.host_ip

    class Meta:
        verbose_name = u"主机记录"
        verbose_name_plural = u"主机记录"
