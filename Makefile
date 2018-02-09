app:
	rm -rf public/
	pip install -r requirements.txt
	cd frontend && yarn install --force && yarn build
	mkdir public && cp -r backend/* public/
	cp -rf frontend/dist/static/ public/app/
	cp -rf frontend/dist/index.html public/app/templates/
	cd public/ && export FLASK_CONFIG=production && \
	python manage.py db init && \
	python manage.py db migrate && \
	python manage.py db upgrade && \
	python manage.py init_all && \
	python manage.py runserver

debug:
	make clean
	pip install -r requirements.txt
	cd frontend && yarn install --force && yarn build
	cd backend && export FLASK_CONFIG=development && \
	python manage.py db init && \
	python manage.py db migrate && \
	python manage.py db upgrade && \
	python manage.py init_all && \
	python manage.py runserver

clean:
	cd backend && rm -rf migrations && rm -rf *.sqlite

f-up:
	cd frontend && yarn build
