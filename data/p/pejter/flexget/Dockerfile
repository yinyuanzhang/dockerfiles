FROM python:3.6

MAINTAINER Piotr Łuczak <piotrluczak1995@gmail.com>

RUN pip install --no-cache-dir \
	flexget \
	transmissionrpc

WORKDIR /flexget
VOLUME /flexget

CMD rm -f /flexget/.config-lock && flexget daemon start
