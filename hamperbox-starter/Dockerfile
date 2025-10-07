## Dockerfile


```dockerfile
FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . /app/


RUN addgroup --system app && adduser --system --ingroup app app


RUN chmod +x /app/entrypoint.sh


USER app


EXPOSE 8000


ENTRYPOINT ["/app/entrypoint.sh"]
```


---
