FROM letsnet/docker-python:pro
LABEL io.boomfunc.env "Local"

USER root

ENV PYTHONUNBUFFERED            1
ENV PYTHONDONTWRITEBYTECODE     1

ADD shortcuts/*     /usr/local/bin/
ADD bin/*           /usr/local/bin/

RUN set -ex \
        \
        && runDeps=' \
            git \
            ssh \
            ' \
        && apt-get update \
        && apt-get install -y $runDeps --no-install-recommends \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*
