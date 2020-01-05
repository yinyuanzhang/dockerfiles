FROM node:6

# Startup scripts
ADD . /usr/src/app
WORKDIR /usr/src/app

RUN npm install -g forever
RUN npm install

COPY docker/nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["forever", "server.js"]
