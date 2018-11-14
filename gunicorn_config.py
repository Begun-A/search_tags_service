import multiprocessing
from os import getenv

# bind adrress
bind = getenv('GUNICORN_BIND', '0.0.0.0:8080')
# forwarded_allow_ips = '*'

# reload workers on code change (usefull for development)
reload = getenv('GUNICORN_RELOAD', True)

# logging
loglevel = getenv('GUNICORN_LOGLEVEL', 'info')

# timeout
timeout = getenv('GUNICORN_TIMEOUT', 600)

# number of workers
workers = getenv('GUNICORN_WORKERS', multiprocessing.cpu_count())
