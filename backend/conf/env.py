import os

from application.settings import BASE_DIR

# ================================================= #
# ************** 数据库 配置  ************** #
# ================================================= #

# 数据库 ENGINE ，默认演示使用 sqlite3 数据库，正式环境建议使用 mysql 数据库
# sqlite3 设置
DATABASE_ENGINE = "django.db.backends.sqlite3"
DATABASE_NAME = os.path.join(BASE_DIR, 'db.sqlite3')

# 使用mysql时，改为此配置
# DATABASE_ENGINE = "django.db.backends.mysql"
# DATABASE_NAME = 'django-vue-admin' # mysql 时使用
# 数据库地址 改为自己数据库地址
DATABASE_HOST = "10.0.90.66"
# # 数据库端口
DATABASE_PORT = 3357
# # 数据库用户名
DATABASE_USER = "root"
# # 数据库密码
DATABASE_PASSWORD = "pO4d4INIarf8Lo9e"

# ================================================= #
# ************** redis配置，无redis 可不进行配置  ************** #
# ================================================= #
# REDIS_PASSWORD = ''
# REDIS_HOST = '127.0.0.1'
# REDIS_URL = f'redis://:{REDIS_PASSWORD or ""}@{REDIS_HOST}:6380'
# ================================================= #
# ************** 其他 配置  ************** #
# ================================================= #
DEBUG = True  # 线上环境请设置为True
ALLOWED_HOSTS = ["*"]
LOGIN_NO_CAPTCHA_AUTH = True  # 登录接口 /api/token/ 是否需要验证码认证，用于测试，正式环境建议取消
ENABLE_LOGIN_ANALYSIS_LOG = True  # 启动登录详细概略获取(通过调用api获取ip详细地址)
