FROM python:3.7-stretch

MAINTAINER michel@rami.io

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y python3 git python3-pip \
	libxml2-dev libxslt1-dev python-dev python-virtualenv locales libffi-dev \
	build-essential python3-dev zlib1g-dev libssl-dev gettext git \
	libpq-dev libjpeg-dev curl --no-install-recommends

RUN dpkg-reconfigure locales && \
	locale-gen C.UTF-8 && \
	/usr/sbin/update-locale LANG=C.UTF-8
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /data
RUN mkdir /code

COPY docker/get-pip.py /tmp/get-pip.py
RUN python3 /tmp/get-pip.py

COPY src/requirements.txt /tmp/requirements.txt
RUN pip install gunicorn -Ur /tmp/requirements.txt

ENV PLUM_DATA_DIR /data
RUN mkdir /code/plum
COPY src /code/plum/src
COPY docker/entrypoint.sh /usr/local/bin/plum
RUN chmod +x /usr/local/bin/plum

WORKDIR /code/plum/src
RUN mkdir /data/logs
ENV DJANGO_SETTINGS_MODULE plum.settings
RUN mkdir /static

RUN /usr/local/bin/plum init

VOLUME /data

EXPOSE 80
ENTRYPOINT ["plum"]
