# 存放开发环境的配置
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development-secret-key'

DEBUG = True

# DEBUG = False

# ALLOWED_HOSTS = ['127.0.0.1','localhost','47.114.52.216','.wpfei.cn']
ALLOWED_HOSTS = ['*']