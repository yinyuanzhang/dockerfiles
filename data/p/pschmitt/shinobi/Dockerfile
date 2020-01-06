FROM ubuntu:xenial
RUN apt update \
    && apt upgrade -y \
    && apt install -y ffmpeg nodejs npm libav-tools wget --no-install-recommends
RUN echo 'mysql-server mysql-server/root_password password night' | debconf-set-selections
RUN echo 'mysql-server mysql-server/root_password_again password night' | debconf-set-selections
RUN apt -y install mysql-server --no-install-recommends
RUN sed -ie "s/^bind-address\s*=\s*127\.0\.0\.1$/#bind-address = 127.0.0.1/" /etc/mysql/mysql.conf.d/mysqld.cnf
RUN sed -ie "s/^port\s*=\s*3306$/port = 3314/" /etc/mysql/mysql.conf.d/mysqld.cnf

RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN mkdir /opt/shinobi
COPY . /opt/shinobi
RUN cp /opt/shinobi/conf.sample.json /opt/shinobi/conf.json
RUN cp /opt/shinobi/super.sample.json /opt/shinobi/super.json
#RUN cp /opt/shinobi/plugins/motion/conf.sample.json /opt/shinobi/plugins/motion/conf.json
RUN chmod -R 755 /opt/shinobi
WORKDIR /opt/shinobi
RUN npm install
RUN npm install pm2 -g
RUN chmod +x ./docker-entrypoint.sh
VOLUME ["/var/log/mysql/","/opt/shinobi/videos"]
EXPOSE 8083
EXPOSE 3314
ENTRYPOINT ./docker-entrypoint.sh