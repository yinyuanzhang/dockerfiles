FROM node:10

ENV APP_HOME /app
RUN mkdir -pv $APP_HOME
WORKDIR $APP_HOME

ADD . $APP_HOME

VOLUME /var/www/html /var/users

RUN cd /var
RUN mkdir users

RUN cd /app
RUN npm install

EXPOSE 3000
CMD [ "npm", "start" ]
