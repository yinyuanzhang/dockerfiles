FROM bytesized/base
MAINTAINER maran@bytesized-hosting.com

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    git \
    nodejs \
    unrar \
    tzdata \
    gcc \
    libffi-dev \
    openssl-dev \
    musl-dev \
    && pip install pyopenssl \
    &&  mkdir /app /var/run/sickchill
RUN git clone https://github.com/SickChill/SickChill.git --depth 2 /app/sickchill

EXPOSE 8081

COPY static/ /

VOLUME /data /config /media
