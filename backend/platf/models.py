from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel
from dvadmin.utils.models import CoreModel, table_prefix

class PlatformModel(CoreModel):
    platform_name = models.CharField(max_length=255, verbose_name="平台名称")
    service_name = models.CharField(max_length=255, verbose_name="服务名称")
    git_url = models.CharField(max_length=255, verbose_name="代码地址")
    Remark = models.CharField(max_length=255, verbose_name="备注说明")

    class Meta:
        db_table = table_prefix + "Platform"
        verbose_name = '平台表'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)