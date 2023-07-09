lint:
	black . && isort .

shell:
	docker exec -it my_site-web-1 /bin/sh -c "python manage.py shell"

ssh:
	docker exec -it my_site-web-1 /bin/sh
