FROM debian:jessie
MAINTAINER Carles Amigó, fr3nd@fr3nd.net

RUN apt-get update && apt-get install -y \
      build-essential \
      curl \
      libcairo2-dev \
      libffi-dev \
      nginx \
      python-dev \
      python-pip \
      supervisor \
      && rm -rf /usr/share/doc/* && \
      rm -rf /usr/share/info/* && \
      rm -rf /tmp/* && \
      rm -rf /var/tmp/*

ENV GRAPHITE_VERSION 0.9.13
ENV GRAPHITE_API_VERSION 1.1

RUN pip install \
      whisper==$GRAPHITE_VERSION \
      carbon==$GRAPHITE_VERSION \
      graphite-api==$GRAPHITE_API_VERSION \
      gunicorn==19.3.0
      #Django==1.8.5 \
      #django-tagging==0.4 \
      #gunicorn==19.3.0

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY carbon.conf /opt/graphite/conf/carbon.conf
COPY storage-schemas.conf /opt/graphite/conf/storage-schemas.conf
COPY storage-aggregation.conf /opt/graphite/conf/storage-aggregation.conf
COPY aggregation-rules.conf /opt/graphite/conf/aggregation-rules.conf
COPY graphite-api.yaml /etc/graphite-api.yaml
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
EXPOSE 2003
EXPOSE 2004
EXPOSE 7002
EXPOSE 2023
EXPOSE 2024

VOLUME /opt/graphite/storage

CMD	/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
