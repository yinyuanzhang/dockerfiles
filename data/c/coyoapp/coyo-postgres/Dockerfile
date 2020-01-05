FROM postgres:9.5.11

ENV REMCO_VER 0.10.0

RUN apt-get update && \
    apt-get install -y unzip wget && \
    wget https://github.com/HeavyHorst/remco/releases/download/v${REMCO_VER}/remco_${REMCO_VER}_linux_amd64.zip && \
    unzip remco_${REMCO_VER}_linux_amd64.zip && rm remco_${REMCO_VER}_linux_amd64.zip && \
    mv remco_linux /bin/remco && \
    apt-get purge -y --auto-remove wget unzip

COPY config/remco /etc/remco
COPY --chown=postgres:postgres config/pg_hba.conf /etc/postgresql/

COPY init.sql /docker-entrypoint-initdb.d/

COPY entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]
CMD ["-c", "config_file=/etc/postgresql/postgresql.conf", "-c", "hba_file=/etc/postgresql/pg_hba.conf"]
