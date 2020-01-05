FROM debian:stretch-slim

ARG BUILD_DATE
ARG VCS_REF

LABEL maintainer                      "Guillaume LAURENT <laurent.guillaume@gmail.com>"
LABEL org.label-schema.build-date     $BUILD_DATE
LABEL org.label-schema.vcs-url        "https://github.com/iamthemitch/docker-wemo.git"
LABEL org.label-schema.vcs-ref        $VCS_REF
LABEL org.label-schema.name           "Belkin WeMo"
LABEL org.label-schema.description    "Container to control Belkin WeMo devices, based on ouimeaux lib"
LABEL org.label-schema.url            "https://ouimeaux.readthedocs.io"
LABEL org.label-schema.schema-version "1.0.0-rc1"

RUN \
  # Packages and system setup
  apt-get update && \
  apt-get install -y \
    curl \
    git gcc \
    python python-pip python-dev && \
  # Create user
  adduser --disabled-password --gecos "Belkin WeMo" wemo && \
  # Pip
  # pip install -U pip && \
  # Lock lib versions - July 30, 2016
  pip install Flask==0.8 && \
  # ouimeaux
  pip install -e 'git+https://github.com/iancmcc/ouimeaux.git#egg=ouimeaux[server]' && \
  # Patch
  sed -i 's#gevent.wsgi#gevent.pywsgi#' /src/ouimeaux/ouimeaux/subscribe.py && \
  # Clean
  apt-get remove --purge -y git gcc && \
  apt-get autoremove -y && apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  echo DONE

EXPOSE  5000
USER    wemo

HEALTHCHECK --interval=5m --timeout=5s \
  CMD curl -f -X GET "http://127.0.0.1:5000/api/environment" || exit 1

ENTRYPOINT ["wemo"]
CMD        ["server"]
