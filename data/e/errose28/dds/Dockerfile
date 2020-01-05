FROM mongo:4.2.1-bionic

RUN apt update && apt install -y python3.7 python3-pip
# Ensure that pip for python3.7 is used.
# Ubuntu uses 3.6 as the default.
RUN python3.7 -m pip install falcon pylint pymongo gunicorn jsonschema

WORKDIR /app

COPY Resource Resource
COPY pylintrc pylintrc

COPY Source Source
RUN pylint Source/*
