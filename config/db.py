import os 

from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SQLITE = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}

POSTGRESQL = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'ryowutest',
    'USER': 'postgres',
    'PASSWORD': 'leo140814',
    'HOST': 'localhost',
    'PORT': '5432'
  }
}