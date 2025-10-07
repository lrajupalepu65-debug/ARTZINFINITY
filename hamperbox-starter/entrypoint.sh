## entrypoint.sh


```bash
#!/bin/sh
set -e


# Apply migrations
python manage.py migrate --noinput


# Create superuser if not exists (using environment variables could be added)


exec "$@"
```


---
