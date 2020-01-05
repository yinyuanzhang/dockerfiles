FROM python:3-alpine
MAINTAINER "EEA: IDM2 A-Team" <eea-edw-a-team-alerts@googlegroups.com>

ENV PYLINT_VERSION=2.2.3

RUN apk add --no-cache --virtual .run-deps git \
 && apk add --no-cache curl \
 && pip install --no-cache-dir anybadge pylint==$PYLINT_VERSION \
 && mkdir -p /code

COPY pylint.cfg /etc/pylint.cfg
COPY docker-entrypoint.sh /
RUN pip install --no-cache-dir https://minio.dev.ftech.ai/axiom-client/axiom_client-1.5.0-py3-none-any.whl

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["pylint"]
