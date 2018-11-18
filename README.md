# Search Tags Service API
Python 3.7
Service provide searching tags in text.

Create environment:
`virtualenv -p python3 .env`

Activate environment:
`source .env/bin/activate`

Install requirements:
`pip install -r requirements.txt`

Run application:
`gunicorn --config ./gunicorn_config.py search_tags_service.instance:app`

Run tests:
`make tests`

**Endpoint for POST rquest:**
  
 _http://127.0.0.1:8080/v1/tags_ 
 
 **JSON example:** 
 
 _{"text": "Example text."}_
 
 **Time performance for 10^6 tags less than 10^(-5)**