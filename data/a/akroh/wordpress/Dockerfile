FROM akroh/apache:2.2

MAINTAINER Andrew Kroh (andy@crowbird.com)

RUN yum -y install tar && yum clean all

# Published at: https://wordpress.org/wordpress-4.1.tar.gz.sha1
ENV WORDPRESS_SHA1 f0437c96ae3d8acaba3579566f1346f4cd06468e

RUN rm -rf /var/www/html/* && \
    curl -o wordpress.tar.gz https://wordpress.org/wordpress-4.1.tar.gz && \
    echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - && \
    tar xf wordpress.tar.gz --strip-components=1 -C /var/www/html && \
    mkdir /var/www/html/wp-content/uploads && \
    chown -R apache:apache /var/www/html/* && \
    rm wordpress.tar.gz

# Separate the wordpress installation to its own volume.
VOLUME /var/www/html/wp-content/uploads
    
COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
