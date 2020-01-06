FROM node:8

RUN apt-get update && apt install python-pip --yes
RUN pip install docker-compose
RUN npm install balena-cli -g --production --unsafe-perm

CMD [ "balena" ]
