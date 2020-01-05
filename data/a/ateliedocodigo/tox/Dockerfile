FROM themattrix/tox-base

MAINTAINER Luis Fernando Gomes <dev@luiscoms.com.br>

RUN apt-get update && apt-get install -y --no-install-recommends git && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ONBUILD COPY README.md install-prereqs*.sh requirements*.txt tox*.ini /app/
ONBUILD ARG SKIP_TOX=false
ONBUILD RUN bash -c " \
    if [ -f '/app/install-prereqs.sh' ]; then \
        bash /app/install-prereqs.sh; \
    fi && \
    if [ $SKIP_TOX == false ]; then \
        TOXBUILD=true tox; \
    fi"

