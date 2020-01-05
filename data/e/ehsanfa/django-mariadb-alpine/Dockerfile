FROM alpine:3.5

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN apk update \
	&& apk add python3 py3-pip nginx openrc py-virtualenv gcc libc-dev linux-headers python3-dev build-base pcre-dev jpeg-dev zlib-dev mariadb-dev 
RUN adduser -D -g 'www' www 
RUN mkdir -p /var/log/uwsgi 
RUN chmod 777 /var/log/uwsgi 

RUN pip3 install -r /tmp/requirements.txt

CMD if [ -d env ]; then echo "env already exists" ; else mkdir env; fi \
	&& virtualenv --system-site-packages env \
	&& source env/bin/activate \
	&& python3 manage.py migrate \
	&& python3 manage.py runserver 0.0.0.0:8000
