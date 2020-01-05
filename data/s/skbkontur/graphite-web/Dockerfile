FROM alpine:3.5

MAINTAINER SKB Kontur <devops@skbkontur.ru>

RUN	apk add --no-cache git nginx supervisor build-base python-dev py-pip py-cffi py-cairo tzdata

RUN	pip install --upgrade pip && pip install django==1.9 \
	twisted==13.1 \
	python-memcached==1.58 \
	incremental==16.10.1 \
	txAMQP==0.7 \
	simplejson==3.11.1 \
	django-tagging==0.4.3 \
	gunicorn \
	pytz \
	pyparsing \
	cairocffi \
	whitenoise \
	scandir \
	urllib3 \
	whisper==1.0.2

RUN	pip install git+https://github.com/graphite-project/graphite-web.git@587a313a045abee470785a8ea5b5edbdcce2da34

RUN	addgroup -S graphite && \
	adduser -S graphite -G graphite && \
	mkdir -p /opt/graphite/webapp/graphite /var/log/graphite /opt/graphite/storage/whisper /var/log/supervisor

ENV	TZ=UTC \
	WHISPER_DIR=/opt/graphite/storage/whisper \
	GRAPHITE_STORAGE_DIR=/opt/graphite/storage \
	GRAPHITE_CONF_DIR=/opt/graphite/conf \
	PYTHONPATH=/opt/graphite/webapp \
	LOG_DIR=/var/log/graphite \
	DEFAULT_INDEX_TABLESPACE=graphite \
	GUNICORN_WORKERS=2

ADD ./config/graphite_wsgi.py /opt/graphite/conf/graphite_wsgi.py
ADD ./config/local_settings.py /opt/graphite/webapp/graphite/local_settings.py
ADD ./config/initial_data.json /opt/graphite/webapp/graphite/initial_data.json
ADD ./config/nginx.conf /etc/nginx/nginx.conf
ADD ./config/supervisord.conf /etc/supervisor/supervisord.conf
ADD ./docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
RUN	chmod +x /usr/bin/docker-entrypoint.sh

# Initialize database(sqlite3)
RUN	cd /opt/graphite/webapp/graphite && django-admin.py migrate --settings=graphite.settings --run-syncdb && \
	cd /opt/graphite/webapp/graphite && django-admin.py loaddata --settings=graphite.settings initial_data.json && \
	touch /opt/graphite/storage/index && \
	chown -R graphite:graphite /opt/graphite /var/log/graphite

WORKDIR /opt/graphite/webapp
EXPOSE 80

CMD ["/usr/bin/docker-entrypoint.sh"]
