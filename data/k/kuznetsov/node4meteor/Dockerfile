FROM node:8.9.3

ENV DEBIAN_FRONTEND noninteractive

RUN \
    curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - &&\
    echo "deb http://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list &&\
    apt-get update &&\
    apt-get -y dist-upgrade &&\
    apt-get -y install graphicsmagick yarn &&\
    apt-get -y autoremove &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    npm update -g

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 80
CMD ["/entrypoint.sh"]
