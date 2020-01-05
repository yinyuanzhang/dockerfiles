FROM python:2.7.15-alpine3.8

RUN apk update && apk add --no-cache build-base gcc git curl wget openjdk8-jre-base
RUN pip install --upgrade pip

RUN git clone --recursive https://github.com/rednaga/yara-python-1.git yara-python
WORKDIR /yara-python
RUN CFLAGS="-std=gnu99" python setup.py build --enable-dex install

RUN mkdir /apkid
COPY ./ /apkid/
WORKDIR /apkid
RUN pip install pypandoc
RUN python prep-release.py
RUN pip install -e .[dev]

# Place to bind a mount point to for scratch pad work
RUN mkdir /input
WORKDIR /input

# Cleanup
RUN rm -rf /var/cache/apk/*