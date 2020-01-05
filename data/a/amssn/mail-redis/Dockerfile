FROM redis:alpine
LABEL maintainer "AMSSN <info@amssn.eu>"
ENV TZ='Europe/Berlin'

ADD data /tmp/
RUN chmod +x /tmp/*.sh ; /tmp/setup.sh

# port provision
EXPOSE 6379/tcp

#CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
CMD [ "redis-server" ]
