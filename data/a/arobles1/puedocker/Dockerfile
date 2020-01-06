FROM debian:9
MAINTAINER Antonio Robles
RUN apt-get update && apt-get install -y apache2 php7.0 php7.0-mysql libapache2-mod-php7.0 wget php-redis && \
    sed -i -e "s/^session.save_handler.*/session.save_handler = redis/" -e "/^session.save_handler/i session.save_path = \"tcp://redis\"" /etc/php/7.0/apache2/php.ini && \
    cd /var/www/html && \
    rm -f index.html && \
    wget https://wordpress.org/latest.tar.gz && \
    tar xzf latest.tar.gz && \
    ln -sf /dev/stdout /var/log/apache2/access.log && \
    ln -sf /dev/stderr /var/log/apache2/error.log && \
    rm -f latest.tar.gz
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
