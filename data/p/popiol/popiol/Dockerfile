FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
php php-curl php-mysqli \
openssh-server

COPY . /app

WORKDIR /app

EXPOSE 80

CMD ["/bin/sh","setup_worker.sh"]

