"""
WSGI config for mnemochoice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

exec(open("../venv/bin/activate_this.py").read(), {'__file__': "/venv/bin/activate_this.py"})

sys.path.append('/venv/core/core')

sys.path.append('/venv/lib/python3.6/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mnemochoice.settings')

application = get_wsgi_application()
