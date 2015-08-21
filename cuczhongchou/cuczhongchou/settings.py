# -*- coding: utf-8 -*-
"""
Django settings for cuczhongchou project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1w2c%*2$4spl^sab_2dos!se3p5nhi!l*0m-*3ace9bg-%lio8'

# SECURITY WARNING: don't run with debug turned on in production!
#开发环境使用
DEBUG = True
#生产环境使用
#DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    ##这句话可以激活/关闭 admin 后台的 bootstrapped 风格
    'django_admin_bootstrapped',
    ##
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'learn',    #自强学社文档学习
    'd01_first_steps', #开始官方文档学习
    #'crowdfunding', # 众筹
    'rest_framework', #rest 架构

)

"""
# rest设置 http://www.django-rest-framework.org/#requirements
激活 DjangoModelPermissionsOrAnonReadOnly 权限设置
  会导致下面错误: Cannot apply DjangoModelPermissions on a view that does not have
    `.queryset` property or overrides the `.get_queryset()` method.
  可以 单独在类的继承中激活permission 或是函数的decorator中使用permission装饰来解决
  母亲

"""
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 管理员 或 匿名用户只读
    #'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
    # 仅管理员 
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    #@api_vew

    'PAGE_SIZE': 10, #定义 -list 翻页数量

}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cuczhongchou.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #增加自定义模板路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cuczhongchou.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 修改为mysql数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
#         },
#     }
# }
# my.cnf 格式如下
"""
[client]
host = HOST
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
"""


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# admin 英文后台 bootstrap 风格更协调一些
LANGUAGE_CODE = 'en-us'
# admin中文后台 TODO 将admin后台的字体缩小
#LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'



#在终端显示日志输出
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'NOTSET',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'NOTSET',
        },
        'django.request': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'ERROR'
        }
    }
}