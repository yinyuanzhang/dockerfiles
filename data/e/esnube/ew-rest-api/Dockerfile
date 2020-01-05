# pull official base image
FROM ubuntu:bionic

# set work directory
WORKDIR /usr/src/app

# copy project
COPY . /usr/src/app/
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        language-pack-es \
        joe \
        libproj-dev \
        gdal-bin \
        python3-pip \
        git \
        python3-setuptools \
        netcat-openbsd

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LC_CTYPE es_ES.UTF-8
ENV LANG es_ES.UTF-8

# django requirements
RUN pip3 install -r requirements.txt

# links
RUN ln -s  /usr/bin/python3.6  /usr/bin/python

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
