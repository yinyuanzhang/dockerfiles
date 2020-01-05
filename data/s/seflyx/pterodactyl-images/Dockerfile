FROM ubuntu:18.04
LABEL author="seflyx" maintainer="josef.livio99@gmail.com"

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install liblua5.1-0 mysql-client libmysqlclient20 \
    && apt-get clean \
    && useradd -m -d /home/container container

USER container
ENV USER=container HOME=/home/container

WORKDIR /home/container

COPY ./entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
