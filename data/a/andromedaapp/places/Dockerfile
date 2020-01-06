FROM node:12
MAINTAINER Giambra Domenico <zorinik@gmail.com>

RUN apt-get update && apt-get -y upgrade

EXPOSE 80

COPY wait-for-it.sh /wait-for-it.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /wait-for-it.sh && chmod +x /entrypoint.sh

COPY app /app

WORKDIR /app
RUN npm ci

ENTRYPOINT ["/entrypoint.sh"]