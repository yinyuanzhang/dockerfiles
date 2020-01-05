FROM python:3
MAINTAINER José Henrique Luckmann

ADD /src /src
ADD requeriments.txt /

RUN pip install -r requeriments.txt
RUN python -m textblob.download_corpora

EXPOSE 8080
WORKDIR /src
