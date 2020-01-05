FROM tiangolo/uwsgi-nginx:python2.7

MAINTAINER Jennifer Liao <cutejaneii@hotmail.com>

ENV NGINX_MAX_UPLOAD 4m
ENV NGINX_WORKER_PROCESSES auto
ENV LISTEN_PORT 8080
EXPOSE 8080

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app

# Set workDir
WORKDIR /app
