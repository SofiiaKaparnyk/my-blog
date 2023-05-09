lint:
	black . && isort . && flake8 my_site/ && flake8 blog/

shell:
	docker exec -it my_site-web-1 /bin/sh -c "python manage.py shell"


