FROM mariadb:10.3.10

LABEL Version=10.3.10 \
      Name=k8s-mariadb-galera

ADD ["galera/", "/opt/galera/"]

RUN set -x && \
    cd /opt/galera && chmod +x on-start.sh galera-recovery.sh

ADD ["docker-entrypoint.sh", "/usr/local/bin/"]
ADD ["peer-finder", "/usr/local/bin/peer-finder"]

EXPOSE 3306/tcp

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["mysqld"]
