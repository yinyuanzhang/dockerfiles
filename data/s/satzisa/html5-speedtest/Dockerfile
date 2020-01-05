FROM php:7.3.1-apache
EXPOSE 80
WORKDIR /tmp
# install packages
RUN apt update && \
    apt install -y git
# Download contents
RUN git clone https://github.com/satzisa/speedtest.git
VOLUME ["/var/www/html"]
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
