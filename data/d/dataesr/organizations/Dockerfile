FROM python:3.6.5-alpine

RUN apk add --no-cache \
	ca-certificates \
	openblas

RUN apk update && apk add netcat-openbsd && apk add g++ gcc libxslt-dev

RUN apk add --no-cache \
        --virtual=.build-dependencies \
        g++ gfortran file binutils \
        musl-dev python3-dev openblas-dev && \
    apk add libstdc++ openblas && \
    \
    ln -s locale.h /usr/include/xlocale.h && \
    \
    pip install --upgrade pip && \
    pip install numpy && \
    pip install scipy && \
    pip install scikit-learn && \
    \
    rm -r /root/.cache && \
    find /usr/lib/python3.*/ -name 'tests' -exec rm -r '{}' + && \
    find /usr/lib/python3.*/site-packages/ -name '*.so' -print -exec sh -c 'file "{}" | grep -q "not stripped" && strip -s "{}"' \; && \
    \
    rm /usr/include/xlocale.h && \
    \
    apk del .build-dependencies

# set working directory
WORKDIR	/srv

# add and install requirements
COPY requirements.txt /srv/requirements.txt
RUN	pip	install -r requirements.txt --proxy=${HTTP_PROXY}

# add app
COPY . /srv
