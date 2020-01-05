FROM postgres:9.5
ADD download_top10nl.sh /opt/download_top10nl.sh
RUN chmod 755 /opt/download_top10nl.sh
RUN /opt/download_top10nl.sh
RUN apt-get update
RUN apt-get -y --force-yes install postgis
ADD scripts/*.* /docker-entrypoint-initdb.d/
