## README.md (short)


```
# HamperBox Starter


Run locally (without Docker):


1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py loaddata shop/fixtures/products.json
6. python manage.py runserver


Run with Docker:


docker-compose up --build


Load seed data inside the running container (if needed):


./load_data.sh
```


---
