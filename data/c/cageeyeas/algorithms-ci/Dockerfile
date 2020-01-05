FROM debian:buster-slim

ENV DEBIAN_FRONTEND="teletype" \
    LANG="C.UTF-8" \
    LANGUAGE="C.UTF-8" \
    LC_ALL="C.UTF-8"

RUN apt-get update && \
    apt-get install --yes python3 python3-dev gcc python3-pip git


ADD requirements.txt requirements.txt
RUN pip3 install wheel "setuptools>=41.0.0" --upgrade
RUN pip3 install -r requirements.txt
