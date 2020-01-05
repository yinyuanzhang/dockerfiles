FROM socialpoint/php:7.2-fpm

ENV SSH_USER root
ENV SSH_PASS root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wget \
        openssh-server \
        supervisor \
        rsync

# SSHD daemon setup as per the official documentation
# at https://docs.docker.com/engine/examples/running_ssh_service/
RUN mkdir -p /var/run/sshd \
 && echo "${SSH_USER}:${SSH_PASS}" | chpasswd \
 && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
 && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN printf "\n\
[supervisord]\n\
nodaemon=true\n\
logfile=/var/log/supervisord.log\n\
pidfile=/var/run/supervisord.pid\n\
\n\
[program:sshd]\n\
command=/usr/sbin/sshd -D\n\
\n\
[program:php-fpm]\n\
command=/usr/local/sbin/php-fpm --nodaemonize\n\
" > /etc/supervisor/conf.d/supervisord.conf

# TODO: Does this make sense? Why allowing to change internal containers behavior ?
RUN printf '#!/usr/bin/env bash\ndocker-php-ext-enable "$@"\n' > /usr/local/sbin/phpenmod \
        && chmod +x /usr/local/sbin/phpenmod \
    && printf '#!/usr/bin/env bash\nrm "/usr/local/etc/php/conf.d/docker-php-ext-$@.ini"\n' > /usr/local/sbin/phpdismod \
        && chmod +x /usr/local/sbin/phpdismod

# Enable xdebug by default
ENV ENABLE_XDEBUG 1

ENV XDEBUG_REMOTE_HOST 127.0.0.1

RUN printf "\nxdebug.remote_host=\${XDEBUG_REMOTE_HOST}\n\
xdebug.default_enable=0\n\
xdebug.idekey=app_docker\n\
xdebug.remote_enable=1\n\
xdebug.remote_autostart=1\n" >> /usr/local/etc/php/conf.d/20-xdebug.ini

RUN composer global require "squizlabs/php_codesniffer" "phpmd/phpmd" "hirak/prestissimo"

# Add the directory where composer put binaries to the system path
ENV PATH="$HOME/.composer/vendor/bin:${PATH}"

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["docker-php-entrypoint", "dockerize"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
