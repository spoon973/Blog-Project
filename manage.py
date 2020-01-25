#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # 如果当前环境中DJANGO_SETTINGS_MODULE的值没有被设置，就将其设置为blogproject.settings
    # 所以当我们使用python manage.py 执行命令的时候，django默认为我们使用了settings.py这个配置
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
