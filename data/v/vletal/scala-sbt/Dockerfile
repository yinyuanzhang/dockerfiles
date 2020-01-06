FROM ubuntu:19.04

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

RUN echo 'tzdata tzdata/Areas select Etc' | debconf-set-selections; \
    echo 'tzdata tzdata/Zones/Etc select UTC' | debconf-set-selections; \
    apt-get update -qqy \
 && apt-get install -qqy --no-install-recommends apt-utils \
 && apt-get install -qqy --no-install-recommends tzdata \
 && apt-get clean

RUN apt-get install -qqy gcc build-essential
RUN apt-get install -qqy postgresql-11 postgresql-server-dev-11
RUN apt-get install -qqy python3 python3-pip python3-virtualenv python3-psycopg2 python3-testing.postgresql \
                         python3-psycopg2 python3-numpy

USER postgres

ENV VIRTUAL_ENV="/var/lib/postgresql/venv"
RUN python3 -m virtualenv --system-site-packages --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"