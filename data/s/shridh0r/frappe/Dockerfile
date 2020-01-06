ARG PYTHON_VERSION=3.7
FROM python:$PYTHON_VERSION-alpine
MAINTAINER Shridhar <shridharpatil2792@gmail.com>
RUN apk add --no-cache git && \
    apk add --no-cache --update nodejs nodejs-npm && \
    apk add --no-cache mysql-client && \
    apk add --no-cache redis && \
    apk add --no-cache openssl-dev libffi-dev && \
    apk add --no-cache libxslt-dev && \
    apk add --no-cache --virtual .build-deps gcc musl-dev && \
    apk add --no-cache build-base python-dev py-pip jpeg-dev zlib-dev && \
    apk add postgresql-client && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install --upgrade pip setuptools wheel && \
    pip install cython && \
    npm install -g yarn

RUN addgroup -g 1000 -S frappe && \
    adduser -u 1000 -S frappe -G frappe

ENV LC_ALL C.UTF-8 && \
    LANG C.UTF-8 && \
    LIBRARY_PATH=/lib:/usr/lib && \
    LC_ALL C.UTF-8 && \

WORKDIR /home/frappe
COPY ./start_up.sh /home/frappe/start_up.sh
RUN chown -R frappe:frappe /home/frappe && \
    chmod 777 /home/frappe && \
    chmod 777 /home/frappe/start_up.sh

# RUN chmod +rwx start_up.sh	

USER frappe
WORKDIR /home/frappe
# VOLUME /home/frappe
ARG FRAPPE_PATH="https://github.com/frappe/frappe.git"
ARG FRAPPE_BRANCH="master"
ARG FRAPPE_PYTHON=python3
ARG FRAPPE="frappe-bench"
ARG DB_HOST="127.0.0.1"
ARG MYSQL_ROOT_PWD="root"
ARG DB_NAME="localsite"
ARG SITE_NAME="site1.local"
ARG BENCH_BRANCH=master
ARG BENCH_PATH=https://github.com/frappe/bench.git 
ENV PATH="${PATH}:/home/frappe/.local/bin" 
ARG CACHE
RUN /bin/sh ./start_up.sh build
WORKDIR /home/frappe/frappe-bench/sites
# RUN /bin/sh ./start_up.sh new_site
# CMD ["/bin/sh", "../start_up.sh", "build"]

CMD ["/home/frappe/frappe-bench/env/bin/gunicorn", "-b", "127.0.0.1:8000", "--workers", "8", "--threads", "4", "-t", "120", "frappe.app:application", "--preload"]
