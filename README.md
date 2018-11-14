# Search Tags Service API
Python 3.7
Service provide searching tags in text.

Create enviroment:
`virtualenv -p python3 .env`

Install requirements:
`pip install -r requirements.txt`

Run application:
`gunicorn --config ./gunicorn_config.py search_tags_service.instance:app`

Run tests:
`make tests`