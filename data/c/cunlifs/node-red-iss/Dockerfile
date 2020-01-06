FROM ubuntu
CMD /bin/bash
MAINTAINER Stuart Cunliffe,UK s_cunliffe@uk.ibm.com
RUN apt-get update
RUN apt-get install -y npm
RUN mkdir -p /usr/src/node-red
WORKDIR /usr/src/node-red
RUN groupadd --force node-red
RUN useradd --home /usr/src/node-red --gid node-red node-red
RUN chown -R node-red:node-red /usr/src/node-red
USER node-red
RUN npm install node-red
EXPOSE 1880/tcp
COPY package.json /usr/src/node-red/package.json
COPY flow-file.json /usr/src/node-red/.node-red/node-red
CMD npm start node-red
