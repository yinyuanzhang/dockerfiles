FROM joomunited/php_cgi:latest

RUN apt-get update && apt-get install -y --no-install-recommends jq
RUN rm -rf /var/lib/apt/lists/*

#Can be latest or any other WP version like 4.9, 5.0, 5.0.2
ENV WORDPRESS_VERSION latest

RUN wget -qO- "https://wordpress.org/wordpress-"$(curl -s 'https://api.wordpress.org/core/version-check/1.7/' | jq "if \"${WORDPRESS_VERSION}\"== \"latest\" then .offers[0].version else .offers[].version | select(. | startswith(\"${WORDPRESS_VERSION}\")) end" | tr -d '"' | head -n 1)".tar.gz" | tar xvz -C /tmp
RUN mv /tmp/wordpress/* /var/www/html

RUN wget -O /usr/local/bin/wp https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
RUN chmod +x /usr/local/bin/wp

RUN chown -R www-data:www-data /var/www/html && \
  find /var/www/html -type d -exec chmod 777 {} \; && \
  find /var/www/html -type f -exec chmod 666 {} \;

RUN /root/set_php_version.sh 5.2

RUN rm -rf /tmp/*

RUN sed -i 's/^Port .*/Port 2222/g' /etc/ssh/sshd_config
RUN sed -i 's/^PermitRootLogin .*/PermitRootLogin yes/g' /etc/ssh/sshd_config

RUN echo "root:password" | chpasswd

RUN rm -rf /var/lib/apt/lists/*

COPY usr/local/bin/ /usr/local/bin/

RUN chmod +x /usr/local/bin/docker_entrypoint.sh

WORKDIR /var/www/html

ENTRYPOINT ["docker_entrypoint.sh"]
CMD ["apache2_foreground.sh"]
