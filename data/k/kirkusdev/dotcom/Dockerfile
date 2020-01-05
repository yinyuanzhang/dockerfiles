FROM alpine:3.9

# copy requirements file
COPY requirements.txt .
COPY requirements_dev.txt .

# MySQL
RUN apk add --no-cache --update python2 python2-dev py-pip py-mysqldb \
    # SSH & BASH
    && apk add --no-cache openssh bash \
    # python pandas
    && apk add --no-cache python-dev py-pip libstdc++ \
    && apk add --no-cache --virtual .build-deps g++ \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    # python lxml
    && apk add --no-cache gcc libc-dev libxslt-dev libxslt libxml2 \
    # Git
    && apk add --no-cache git \
    # Python Pillow
    && apk add --no-cache jpeg-dev zlib-dev \
    # install dependencies:
    && pip --no-cache-dir install --upgrade pip \
    && pip --no-cache-dir install -r requirements_dev.txt \
    # Clean up
    && apk del .build-deps

RUN addgroup -g 1000 app && \
    adduser -D -u 1000 -G app app

USER app

WORKDIR /app
