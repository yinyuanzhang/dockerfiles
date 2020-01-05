FROM joomunited/php_cgi:latest

RUN apt-get update && apt-get install -y --no-install-recommends jq git
RUN rm -rf /var/lib/apt/lists/*

ENV JOOMLA_VERSION latest

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" &&\
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/local/bin/composer

RUN composer global require joomlatools/console && \
    ln -s /root/.composer/vendor/bin/joomla /usr/local/bin/joomla

RUN /root/set_php_version.sh 5.3

RUN rm -rf /tmp/*

RUN sed -i 's/^Port .*/Port 2222/g' /etc/ssh/sshd_config
RUN sed -i 's/^PermitRootLogin .*/PermitRootLogin yes/g' /etc/ssh/sshd_config

RUN echo "root:password" | chpasswd

RUN rm -rf /var/lib/apt/lists/*

COPY usr/local/bin/ /usr/local/bin/
ADD	root/* /root/

RUN chmod +x /usr/local/bin/docker_entrypoint.sh

WORKDIR /var/www/html

ENTRYPOINT ["docker_entrypoint.sh"]
CMD ["apache2_foreground.sh"]
