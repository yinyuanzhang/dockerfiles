FROM python:3.8.1-alpine

LABEL maintainer="Ludovic Ortega mastership@hotmail.fr"

# update package
RUN apk update

# install package required by pillow
RUN apk add build-base \
    jpeg-dev \
    zlib-dev

# copy program and requirements
COPY * /app/backend/

# install dependencies
RUN pip3 install -r /app/backend/requirements.txt

# install gunicorn
RUN pip3 install gunicorn

# set workdir
WORKDIR /app/backend/
