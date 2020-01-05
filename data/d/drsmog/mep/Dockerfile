FROM ubuntu:rolling

#install elasticsearch
RUN apt-get update \ 
    && apt-get install --allow-unauthenticated -y default-jre \ 
    && apt-get install --allow-unauthenticated -y wget \ 
    && wget --no-check-certificate https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.3.1/elasticsearch-2.3.1.deb \ 
    && dpkg -i elasticsearch-2.3.1.deb \ 
    && echo "network.host: 0.0.0.0" | tee -a /etc/elasticsearch/elasticsearch.yml \
    && echo "index.max_result_window: 2147483647" | tee -a /etc/elasticsearch/elasticsearch.yml



#install mongodb
RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list \ 
    && apt-get update \ 
    && apt-get install --allow-unauthenticated -y mongodb-org \ 
    && mkdir -p /data/db \ 
    && chown -R mongodb:mongodb /data/db



# install postgresql
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ zesty-pgdg main" >> /etc/apt/sources.list.d/pgdg.list \ 
    && apt-get update \ 
    && apt-get install --allow-unauthenticated -y apt-utils postgresql-10 nano \
    && sed -i "s/local   all             postgres                                peer/local   all             postgres                                trust/g" /etc/postgresql/10/main/pg_hba.conf \ 
    && sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/10/main/postgresql.conf \ 
    && echo "host    all             all             0.0.0.0/0               md5" | tee -a /etc/postgresql/10/main/pg_hba.conf \ 
    && service postgresql start \ 
    && psql -U postgres -c "CREATE ROLE root WITH LOGIN PASSWORD '123456789' SUPERUSER;" \ 
    && service postgresql restart \ 
    && echo "Up And Done"

# install nodejs
RUN apt-get update; exit 0 
RUN apt-get install --allow-unauthenticated -y curl xz-utils \ 
    && curl -SLO --insecure "https://nodejs.org/dist/v8.7.0/node-v8.7.0-linux-x64.tar.xz" \ 
    && tar -xJf "/node-v8.7.0-linux-x64.tar.xz" -C /usr/local --strip-components=1 \ 
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs

COPY boot.sh /usr/local/bin/
RUN ln -s usr/local/bin/boot.sh / # backwards compat
RUN chmod +x boot.sh
ENTRYPOINT  boot.sh ; /bin/bash