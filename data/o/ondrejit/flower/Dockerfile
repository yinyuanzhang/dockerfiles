# vim:set ft=dockerfile:

FROM docker.io/python:3.6-alpine
MAINTAINER Ondrej Barta <ondrej@ondrej.it>

RUN \
	apk --no-cache add tzdata && \

	pip install --no-cache-dir \
	redis \
	https://github.com/mher/flower/zipball/master

USER nobody

EXPOSE 5555

ENTRYPOINT ["flower"]
