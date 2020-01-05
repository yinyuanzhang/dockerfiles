FROM grokon/php:7.1.21
# set mainainer
LABEL maintainer="Grokon"
# add supervisor
RUN apt-get update && apt-get install -q -y --no-install-recommends supervisor && \
    apt-get clean all && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc
# turn off daemon mode
RUN sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf
# add php config
COPY conf/php.ini /usr/local/etc/php/php.ini
# Define working directory.
WORKDIR /etc/supervisor/conf.d
# Define default command.
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]