FROM ubuntu:latest
LABEL maintainer="Gor Pogossian gor@poghosyan.am"
LABEL description="An image for autobuilding test"

ENV TIMEZONE Asia/Yerevan
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install apache2 php -y && \
    ln -fs /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    rm /var/www/html/index.html
    
EXPOSE 80/tcp

ENTRYPOINT ["apachectl"]

CMD ["-D", "FOREGROUND"]
