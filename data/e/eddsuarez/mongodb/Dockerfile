FROM debian:jessie

RUN groupadd -r mongodb && useradd -r -g mongodb mongodb

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv A15703C6 && \
    echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list && \
    apt-get update && \
    apt-get install -y --force-yes pwgen mongodb-org mongodb-org-server mongodb-org-shell mongodb-org-mongos mongodb-org-tools && \
    echo "mongodb-org hold" | dpkg --set-selections && echo "mongodb-org-server hold" | dpkg --set-selections && \
    echo "mongodb-org-shell hold" | dpkg --set-selections && \
    echo "mongodb-org-mongos hold" | dpkg --set-selections && \
    echo "mongodb-org-tools hold" | dpkg --set-selections

RUN mkdir -p /mongodb/data/db \
  && chown -R mongodb:mongodb /mongodb/data/db

VOLUME /mongodb/data/db

ENV AUTH no
ENV STORAGE_ENGINE wiredTiger
ENV JOURNALING yes


ADD run.sh /run.sh
ADD set_mongodb_password.sh /set_mongodb_password.sh

EXPOSE 27017
USER mongodb
CMD ["/run.sh"]