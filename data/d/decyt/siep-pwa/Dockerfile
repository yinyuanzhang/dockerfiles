FROM node:alpine
ADD ./webpack /siep-pwa/
WORKDIR /siep-pwa/

# Descarga el ultimo estado de los commit en los repo developer y master
RUN wget https://api.github.com/repos/decyt-tdf/siep-pwa/commits/master && mv master /siep-pwa/static/master.json
RUN wget https://api.github.com/repos/decyt-tdf/siep-pwa/commits/developer && mv developer /siep-pwa/static/developer.json

# HOTFIX Python
RUN apk add --no-cache python python-dev python3 python3-dev \
    linux-headers build-base bash git ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

RUN npm install
CMD ["sh","/siep-pwa/docker_init.sh"]

