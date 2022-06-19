"""
WSGI config for tendera project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tendera.settings')

application = Cling(get_wsgi_application())
# application = get_wsgi_application()


# import os
# from django.core.wsgi import get_wsgi_application
# from dj_static import Cling
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ََAPPNAME.settings')
# application = Cling(get_wsgi_application())
