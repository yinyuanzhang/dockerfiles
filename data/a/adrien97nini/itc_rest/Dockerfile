FROM greyltc/lamp

MAINTAINER Virginie Van den Schrieck <v.vandenschrieck@ephec.be>

#Script creating the mysql database and the table that receives humidity values
ADD setupMysqlDB.sh /usr/sbin/setup-mysql-db

#Adding api.php file to web server root folder
ADD www /srv/http/

#We don't use HTTP for simplicity - Don't do that in production!
ENV APACHE_ENABLE_PORT_80 true

EXPOSE 80

CMD start-servers; setup-mysql-user; setup-mysql-db; sleep infinity

