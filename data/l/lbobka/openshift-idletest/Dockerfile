FROM ubuntu:trusty
MAINTAINER Lars Bobka <lars.bobka@gmail.com>

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat

USER 1001
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["0"] # in seconds (0=endless loop)
