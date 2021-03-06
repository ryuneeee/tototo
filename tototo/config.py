# -*- coding: utf-8 -*-
import os
import pytz

DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_RED_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
TIMEZONE = pytz.timezone('Asia/Seoul')
