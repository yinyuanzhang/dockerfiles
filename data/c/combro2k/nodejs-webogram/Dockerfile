FROM node:latest

WORKDIR /usr/src/app

ADD https://github.com/zhukov/webogram/archive/master.zip /usr/src/master.zip
RUN apt-get update && apt-get dist-upgrade -yq && apt-get install unzip -yq
RUN unzip /usr/src/master.zip -d /usr/src
RUN rm -fr /usr/src/app && mv /usr/src/webogram-master /usr/src/app

ADD start.sh /usr/src/app/start.sh
RUN chmod +x /usr/src/app/start.sh

# install your application's dependencies
RUN npm install -g gulp && npm install

# replace this with your application's default port
EXPOSE 8000

# replace this with your main "server" script file

CMD [ "/usr/src/app/start.sh" ]
