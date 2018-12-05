"""
Django settings for planc project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '54b1(@lb7s--d3dn$%+xb#$id2v0c$9#cyjo4gt-c=@r(5-2o('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1","192.168.133.128"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.catauth',
    'apps.cms',
    'apps.news',
    'apps.ueditor',
    'rest_framework',
    'debug_toolbar',
    'haystack',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'planc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':['django.templatetags.static'],
        },
    },
]

WSGI_APPLICATION = 'planc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orm_cat2',
        'USER' : 'root',
        'PASSWORD' : '1234',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
    }
}

CACHES = {
    'default' : {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

AUTH_USER_MODEL = 'catauth.Front_User'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

UEDITOR_UPLOAD_TO_SERVER = True
UEDITOR_UPLOAD_PATH = MEDIA_ROOT
UEDITOR_CONFIG_PATH =os.path.join(BASE_DIR,'static','ueditor','config.json')

# 一次加载多少篇新闻文章
ONE_PAGE_NEWS_COUNT = 2

# Django-Debug-Toolbar相关的配置
INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_PANELS = [
    # 代表是哪个django版本
    'debug_toolbar.panels.versions.VersionsPanel',
    # 用来计时的，判断加载当前页面总共花的时间
    'debug_toolbar.panels.timer.TimerPanel',
    # 读取django中的配置信息
    'debug_toolbar.panels.settings.SettingsPanel',
    # 看到当前请求头和响应头信息
    'debug_toolbar.panels.headers.HeadersPanel',
    # 当前请求的想信息（视图函数，Cookie信息，Session信息等）
    'debug_toolbar.panels.request.RequestPanel',
    # 查看SQL语句
    'debug_toolbar.panels.sql.SQLPanel',
    # 静态文件
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    # 模板文件
    'debug_toolbar.panels.templates.TemplatesPanel',
    # 缓存
    'debug_toolbar.panels.cache.CachePanel',
    # 信号
    'debug_toolbar.panels.signals.SignalsPanel',
    # 日志
    # 'debug_toolbar.panels.logging.LoggingPanel',
    # 重定向
    # 'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/js/jquery-3.3.1.min.js',
    'INSERT_BEFORE':"</body>",
}

#设置搜索引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        # 设置haystack的搜索引擎
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'ENGINE': 'apps.news.whoosh_cn_backend.WhooshEngine',

        # 设置索引文件的位置
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

#增删改查后，自动创建索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'