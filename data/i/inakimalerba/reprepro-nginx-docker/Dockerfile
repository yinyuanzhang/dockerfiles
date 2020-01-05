from debian:unstable

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y eatmydata --no-install-recommends

RUN apt-get update && eatmydata apt-get install -y reprepro nginx --no-install-recommends

RUN mkdir -p /var/www/debian/conf/
COPY distributions /var/www/debian/conf/distributions

RUN reprepro -b /var/www/debian export sid && \
    reprepro -b /var/www/debian export buster && \
    reprepro -b /var/www/debian export stretch && \
    reprepro -b /var/www/debian export jessie

EXPOSE 80
