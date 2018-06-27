from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='m^rk@ud(8b$y(b-p2ks#&s%@t3fe^pvg_&47gq7vxxq^@87w@v')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
