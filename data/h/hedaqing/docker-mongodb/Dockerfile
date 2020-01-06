FROM ubuntu:14.04

RUN groupadd -r mongodb && useradd -r -g mongodb mongodb
RUN apt-get update && apt-get install -y mongodb && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /data/db /data/configdb && chown -R mongodb:mongodb /data/db /data/configdb


COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
USER mongodb
EXPOSE 27017
CMD ["mongod"]
