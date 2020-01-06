FROM keymetrics/pm2:8-alpine
LABEL maintainer="SNE <contact@sn-ecommerce.fr>"
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# Install app dependencies
COPY package*.json /usr/src/app/
COPY pm2.json /usr/src/app/
ENV NPM_CONFIG_LOGLEVEL warn
RUN npm install --production
# Bundle app source
COPY . /usr/src/app
RUN npm run build
EXPOSE 3000
CMD [ "pm2-docker", "start", "pm2.json" ]