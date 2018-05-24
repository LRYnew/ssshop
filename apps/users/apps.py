from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户管理'

    # 重载signals 信号量
    def ready(self):
        import users.signals
