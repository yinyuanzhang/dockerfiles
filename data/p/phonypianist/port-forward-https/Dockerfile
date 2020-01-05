FROM node:11

EXPOSE 443

RUN npm install -g mapport

CMD mapport 443 $REMOTE_HOST:$REMOTE_PORT
