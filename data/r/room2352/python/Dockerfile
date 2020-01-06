FROM python:3.6.10-slim

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
# Python, don't write bytecode!
ENV PYTHONDONTWRITEBYTECODE 1

# -- Install Pipenv:
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		curl \
	&& apt-get clean

RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python3.6

# Backwards compatility.
RUN rm -fr /usr/local/bin/python3 && ln /usr/local/bin/python3.6 /usr/local/bin/python3

RUN pip3 install --no-cache-dir pipenv

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app

# -- Install build deps and python packages:
ONBUILD COPY build-deps.in build-deps.in
ONBUILD COPY requirements.txt requirements.txt

ONBUILD RUN set -ex \
	&& apt-get update && cat build-deps.in | xargs apt-get install -y --no-install-recommends \
	&& pip install --no-cache-dir -r requirements.txt \
	&& cat build-deps.in | xargs apt-get purge -y \
	&& apt-get autoremove -y && apt-get clean

# -- Install runtime dependencies:
ONBUILD COPY runtime-deps.in runtime-deps.in
ONBUILD RUN set -ex \
	&& cat runtime-deps.in | xargs apt-get install -y --no-install-recommends \
	&& apt-get clean


# --------------------
# - Using This File: -
# --------------------

# FROM room2352/python:py3.6-slim

# COPY . /app

# -- Replace with the correct path to your app's main executable
# CMD python3 main.py

