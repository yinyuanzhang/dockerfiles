FROM node:10.15-slim
MAINTAINER pihizi@msn.com

ENV LABMAI_RUN_ENV="production"

RUN npm install pm2 -g

RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app

# ADD . /usr/src/app
ADD init.sh /init.sh
RUN chmod 755 /init.sh
ADD rebuild.sh /rebuild.sh
RUN chmod 755 /rebuild.sh
ADD run.sh /run.sh
RUN chmod 755 /run.sh

EXPOSE 8083

# CMD ["npm", "run", "start"]
CMD ["/run.sh"]
