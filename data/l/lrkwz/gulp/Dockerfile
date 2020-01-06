FROM node:alpine

RUN npm install -g bower gulp gulp-cli gulp-sass gulp-install

ADD startup.sh /
RUN chmod +x /startup.sh

WORKDIR /var/www/html

ENTRYPOINT ["/startup.sh"]
