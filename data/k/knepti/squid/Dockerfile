FROM ubuntu-debootstrap:latest

MAINTAINER knepti <knepti@gmail.com>

RUN apt-get update && \
    apt-get install -y squid apache2-utils

ADD squid.conf /etc/squid3/squid.conf

EXPOSE 3128

ENTRYPOINT ["squid3"]

CMD ["-N"]
