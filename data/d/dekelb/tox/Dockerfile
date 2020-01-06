FROM alpine
MAINTAINER Omer Cohen <docker+tox@omer.io>

RUN apk --no-cache add build-base python2 python2-dev python3 python3-dev libffi-dev openssl-dev git && \
	wget -qO- https://bootstrap.pypa.io/get-pip.py | python2 && \
	wget -qO- https://bootstrap.pypa.io/get-pip.py | python3 && \
	pip install tox tox-travis paramiko && pip2 install paramiko

WORKDIR /app
VOLUME /app

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

ENV CMD tox
CMD ["tox"]
