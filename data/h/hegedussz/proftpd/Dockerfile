FROM debian:buster

ENV DEBIAN_FRONTEND noninteractive

# Set timezone
ENV TZ=Europe/Budapest
RUN ln -snf /usr/share/zoneinfo/Europe/Budapest /etc/localtime && echo Europe/Budapest > /etc/timezone

RUN apt-get update \
    && apt-get install -y proftpd mc nano \
    && apt-get clean autoclean \
    && apt-get autoremove --yes  \
    && rm -rf /var/lib/apt/lists/*

RUN sed -i "s/# DefaultRoot/DefaultRoot/" /etc/proftpd/proftpd.conf


EXPOSE 20 21

COPY docker-entrypoint.sh /usr/local/sbin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]

CMD ["proftpd", "--nodaemon"]
