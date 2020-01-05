FROM ubuntu:xenial
MAINTAINER kyoungrok.jang@gmail.com

# mongodb-clients, postgresql-client
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \
    echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \
    apt-get update && \ 
    apt-get install -y postgresql-client mongodb-org-tools

COPY run-backup.sh /
RUN chmod +x /run-backup.sh
CMD ["/run-backup.sh"] 
