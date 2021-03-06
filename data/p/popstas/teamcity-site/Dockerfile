FROM ubuntu:14.04


RUN apt-get update && apt-get install -y openssh-server wget git python python-pip curl mailtools cron vim sendmail-bin
RUN mkdir /var/run/sshd
RUN echo 'root:teamcity' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config


# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd


ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile


# percona
RUN echo percona-server-server-5.5 percona-server-server/root_password password teamcity | debconf-set-selections && \
echo percona-server-server-5.5 percona-server-server/root_password_again password teamcity | debconf-set-selections && \
wget -O - http://www.percona.com/downloads/RPM-GPG-KEY-percona | apt-key add - && \
echo "deb http://repo.percona.com/apt squeeze main" >> /etc/apt/sources.list
RUN echo "[client]" >> /root/.my.cnf && \
echo "user=root" >> /root/.my.cnf && \
echo "password=teamcity" >> /root/.my.cnf
RUN apt-get update && apt-get install -y percona-server-server-5.5 percona-server-client-5.5


# bats
#RUN git clone https://github.com/sstephenson/bats.git /usr/local/src/bats && \
#cd /usr/local/src/bats && \
#./install.sh /usr/local


# php
RUN apt-get install -y php5 php5-mysql php5-gd php5-curl


# composer
RUN echo "suhosin.executor.include.whitelist = phar" >> /etc/php5/cli/conf.d/suhosin.ini && \
curl -sS https://getcomposer.org/installer | php && \
mv composer.phar /usr/local/bin/composer && \
ln -s /usr/local/bin/composer /usr/bin/composer


# drush7
RUN git clone https://github.com/drush-ops/drush.git /usr/local/src/drush7 && \
cd /usr/local/src/drush7 && \
git checkout 7.x && \
ln -s /usr/local/src/drush7/drush /usr/bin/drush && \
composer update && \
composer install


# drush6
RUN git clone https://github.com/drush-ops/drush.git /usr/local/src/drush6 && \
cd /usr/local/src/drush6 && \
git checkout 6.x && \
ln -s /usr/local/src/drush6/drush /usr/bin/drush6 && \
composer update && \
composer install


COPY entrypoint.sh /
COPY mysql_import /usr/local/bin/


EXPOSE 22
EXPOSE 80
EXPOSE 3306


WORKDIR /var/www
CMD ["/entrypoint.sh"]
