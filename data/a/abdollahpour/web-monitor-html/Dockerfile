FROM node:5.12.0
MAINTAINER Hamed Abdollahpour <ha.hamed@gmail.com>

WORKDIR /opt

# Setup nodejs packages
RUN npm config set registry https://registry.npm.taobao.org/
ADD package.json ./
RUN npm install

# HTMLs and bower
ADD public public
RUN npm -g install bower
RUN npm -g install mithril_component_tools
RUN cd public/ && bower install --allow-root && cd -

# Congigurations and code
ADD app.js config.js keycloak.json ./
ADD mithril_components mithril_components
ADD lib lib

ENV LANG EN

RUN mct publish .

EXPOSE 8080

CMD "node" "publish/app.js"