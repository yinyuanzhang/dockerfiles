FROM debian:buster-slim

ENV DEBIAN_FRONTEND="teletype" \
    LANG="C.UTF-8" \
    LANGUAGE="C.UTF-8" \
    LC_ALL="C.UTF-8"

RUN apt-get update && \
    apt-get install --yes python3 python3-dev gcc python3-pip git netcat

ADD requirements.txt requirements.txt
ADD algo_requirements.txt algo_requirements.txt

RUN pip3 install wheel "pytest-mock==1.10.4" "setuptools>=41.0.0" --upgrade
RUN pip3 install -r requirements.txt
RUN pip3 install -r algo_requirements.txt
