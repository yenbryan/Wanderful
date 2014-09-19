DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wanderful',
    }
}

INTERNAL_IPS = ("127.0.0.1", "10.0.2.2")
#POSTGIS_VERSION = (2, 0, 3)