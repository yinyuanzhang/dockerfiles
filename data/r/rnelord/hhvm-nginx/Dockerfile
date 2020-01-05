FROM ubuntu

ENV HHVM_VERSION=3.9.1~trusty

RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    software-properties-common

RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449 \
    && add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"

RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    hhvm=$HHVM_VERSION \
    nginx

RUN /usr/bin/update-alternatives \
    --install /usr/bin/php php /usr/bin/hhvm 60

RUN /usr/share/hhvm/install_fastcgi.sh

COPY config/default /etc/nginx/sites-available/default
COPY config/nginx.conf /etc/nginx/nginx.conf

RUN touch /mnt/.hhconfig
EXPOSE 80
EXPOSE 443
VOLUME /mnt/code

COPY entrypoint.sh /
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx"]
