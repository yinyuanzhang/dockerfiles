FROM ubuntu:18.10

RUN apt-get update -qy

RUN apt-get install -qy hugo

ADD site site

WORKDIR site

CMD hugo server -D --bind=0.0.0.0 --baseURL=https://myhappylittlekitchen.com/ --appendPort=false
