FROM lucacri/alpine-base:3.10
LABEL maintainer="lucacri@gmail.com"


RUN apk --no-cache add \
curl \
nano \
bzip2 \
bash 

ADD rootfs /

EXPOSE 3128
ENV NOTIFY_URL "http://urlhere"
ENV NOTIFY_EVERY_SECONDS 20