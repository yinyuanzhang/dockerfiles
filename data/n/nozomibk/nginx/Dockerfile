FROM nginx

RUN apt-get update && \
        apt-get install -y php-gd libpcre3-dev php-dev make php-pear php-curl php-mcrypt php-mysql php-sqlite3 php-xsl php-fpm php-ldap php-mail && \
        rm -rf /var/lib/apt/lists/*

ADD start.sh /etc/nginx/start.sh

RUN chmod +x /etc/nginx/start.sh

CMD ["/etc/nginx/start.sh"]

