FROM node
MAINTAINER Adrian Balcan

RUN chown -R www-data:www-data /var/log
RUN npm i cloudcmd -g

USER www-data
CMD cloudcmd
