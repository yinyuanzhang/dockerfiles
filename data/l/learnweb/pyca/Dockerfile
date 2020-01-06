FROM debian:jessie-backports
MAINTAINER Jan Koppe <post@jankoppe.de>

ENV OPENCAST_HOST="localhost"
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    git \
    python-dev \
    libcurl4-gnutls-dev \
    gnutls-dev \
    ca-certificates \
    build-essential \
    python-sqlalchemy \
    python-flask \
    python-pycurl \
    python-configobj \
    python-dateutil

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends -t jessie-backports \
    ffmpeg

WORKDIR /pyca

RUN git clone https://github.com/opencast/pyCA .

COPY ./run.sh .

CMD ./run.sh
