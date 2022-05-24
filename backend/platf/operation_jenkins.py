from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import PlatformModel


@receiver(post_save, sender=PlatformModel)  # Django的信号机制
# sender是发出信号的对象 ，instance 是AUTH_USER_MODEL表新增的数据的对象，created 是不是往AUTH_USER_MODEL表新增数据
def add_jenkins_job(sender, instance=None, created=False, **kwargs):
    """
    创建平台信息时自动创建 Jenkins job
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    # 只有 PlatformModel表创建的时候执行
    if created:
        print(instance)
# post_save.connect(add_jenkins_job, sender=PlatformModel)
