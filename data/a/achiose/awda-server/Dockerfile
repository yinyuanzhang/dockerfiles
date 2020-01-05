FROM node:latest
WORKDIR /awda-server
COPY package.json /awda-server
ADD . /awda-server
RUN npm install
EXPOSE 3001
CMD [ “npm”, “start” ]
