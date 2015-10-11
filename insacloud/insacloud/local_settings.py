from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'insacloud',
        'USER': 'insacloud',
        'PASSWORD': 'insacloud',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            'localhost:6379',
        ]
    }
}

# to variabilize
STATIC_ROOT = '/tmp/static'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# persitance in db => 2 redis or keep that
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
STATIC_URL = 'http://localhost:8080/static/'