"""
WSGI config for com_1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'com_1.settings')
SECRET_KEY = os.environ.get( 'django-insecure-%io=dbe(3=t4ic5*c&b_5r@q4-))di0p)5ikvxni*tv@xgg#l5')
application = get_wsgi_application()
