# django_instagram

Simple instagram application on Django Framework  
[![Build Status](https://travis-ci.com/qwanysh/django_instagram.svg?branch=master)](https://travis-ci.com/qwanysh/django_instagram)

### Installation
```bash
virtualenv -p python3 venv  
source venv/bin/activate  
pip3 install -r requirements.txt
cd instagram  
python3 manage.py migrate
python3 manage.py createsuperuser 
```

### Run server

```bash
source venv/bin/activate  
cd instagram   
python3 manage.py runserver  
```

### Run tests

```bash
source venv/bin/activate  
cd instagram  
pytest -vvv
```
