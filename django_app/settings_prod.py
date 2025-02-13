# EB(EC2) 운영환경
from .settings import *

# 운영환경에서는 반드시 False로 설정
DEBUG = True

ALLOWED_HOSTS = [
    'eb-django-app-env.eba-fz43szeq.ap-northeast-2.elasticbeanstalk.com',
    'shqkel.space',
]