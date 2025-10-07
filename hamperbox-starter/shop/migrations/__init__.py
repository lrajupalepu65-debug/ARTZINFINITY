```python
# intentionally empty — run `python manage.py makemigrations shop` to create migrations
```


---


## Additional notes & next steps


- This scaffold uses SQLite and local media (no external DB). Put any sample images into `shop/static/shop/sample_images/` and create ProductImage rows via Django admin or a short management command.
- To create migrations: `python manage.py makemigrations && python manage.py migrate` (Docker will already run migrate in entrypoint)
- To create a superuser: `python manage.py createsuperuser` (or add automation to entrypoint if you want an auto superuser for dev)
- If you'd like, I can now: generate actual migration files, a small management command to import images from `shop/static/shop/sample_images/`, or a tiny script that programmatically creates ProductImage objects pointing to local files and assigns them to products — tell me which and I'll add it to the repo.




---
