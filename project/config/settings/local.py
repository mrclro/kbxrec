from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='+_8_py8uw4be=xv_mc8x=_efgck-41rl6dq+3s%aoa%6bxjp33')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
