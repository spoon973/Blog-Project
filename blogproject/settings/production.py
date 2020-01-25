# 存放线上环境的配置
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # SECRET_KEY是从环境变量中获取的

DEBUG = False  # DEBUG模式关闭

# ALLOWED_HOSTS = ['127.0.0.1','localhost','47.114.52.216','.wpfei.cn']
ALLOWED_HOSTS = ['www.wpfei.cn','47.114.52.216']  # ALLOWED_HOSTS设置了允许的HTTP HOSTS