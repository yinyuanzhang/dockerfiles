FROM python:3.7
LABEL maintainer="dongeon.kim@handys.co.kr"

RUN set -ex && mkdir /resources
WORKDIR /resources

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install zip -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
