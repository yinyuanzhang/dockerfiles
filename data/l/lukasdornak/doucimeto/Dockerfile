FROM lukasdornak/djuwinx:1.0

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=doucimeto.settings
ENV LIBRARY_PATH=/lib:/usr/lib

RUN apk add --update --no-cache postgresql-dev jpeg-dev; \
    apk add --update --no-cache --virtual .build-deps \
		build-base \
		zlib-dev; \
	pip3 install --no-cache-dir -r /app/requirements.txt; \
	apk del .build-deps; \
	rm /app/requirements.txt

RUN django-admin collectstatic \
    && mkdir /app/media \
    && chown nginx /app/media

ENTRYPOINT uwsgi --ini /etc/uwsgi/djuwinx_uwsgi.ini && nginx && /bin/ash
