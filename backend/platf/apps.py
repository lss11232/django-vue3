from django.apps import AppConfig


class PlatfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'platf'
    # 注意使用信号量，需要添加下面信息
    def ready(self):
        from . import operation_jenkins