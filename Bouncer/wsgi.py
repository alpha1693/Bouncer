"""
WSGI config for Bouncer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('C:/Users/Work/Bitnami Django Stack projects/Bouncer')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/Work/Bitnami Django Stack projects/Bouncer/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bouncer.settings")

application = get_wsgi_application()
