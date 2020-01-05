FROM node:10.15
MAINTAINER Mauro Novillo <mauron@beatcoding.com>
ARG PASS_GIT

# Bundle APP files
WORKDIR vallecitos-backend
# Install app dependencies
COPY  ./ .
ENV NPM_CONFIG_LOGLEVEL warn
ENV DB_CONNECTION mongodb://mongo:27017
RUN npm install pm2 -g
RUN npm install --production
RUN npm install --prefix dashboard
RUN npm run build-prod --prefix dashboard
# Show current folder structure in logs
RUN ls -al 
EXPOSE 3000
CMD [ "pm2-runtime", "start", "index.js" ]
