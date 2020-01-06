FROM node:10.4

COPY *.json /var/www/

WORKDIR /var/www
RUN npm install

COPY *.js /var/www/
COPY css /var/www/css
COPY source /var/www/source
COPY templates /var/www/templates

CMD ["npm", "start"]
