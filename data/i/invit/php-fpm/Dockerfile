FROM invit/php-env:7.2.12-r1

MAINTAINER Toni Rudolf <toni.rudolf@weekend4two.com>

ENV DEBIAN_FRONTEND noninteractive

RUN curl -sSL https://download.newrelic.com/php_agent/release/newrelic-php5-8.4.0.231-linux.tar.gz | tar -C /tmp -zx \
    && NR_INSTALL_USE_CP_NOT_LN=1 NR_INSTALL_SILENT=1 /tmp/newrelic-php5-*/newrelic-install install \
    && rm -rf /tmp/newrelic-php5-* /tmp/nrinstall* \
    && cp /etc/newrelic/newrelic.cfg.template /etc/newrelic/newrelic.cfg

COPY symfony.pool.conf /usr/local/etc/php-fpm.d/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.php-fpm.conf
COPY start.sh /start.sh

ENTRYPOINT ["/start.sh"]
CMD ["/usr/bin/supervisord", "--nodaemon"]
