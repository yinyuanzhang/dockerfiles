FROM node

RUN mkdir /src
WORKDIR /src

RUN apt-get update 
RUN apt-get install -y zip

#RUN wget https://circle-artifacts.com/gh/rupalimehta/piyushcircleci/4/artifacts/0/tmp/circle-artifacts.VS2dlWf/nodemod/nodemodules.zip
#RUN unzip nodemodules.zip -d /node_modules
#RUN ls -a /node_modules

ADD html html
ADD test test
ADD circle.yml package.json app.js ./


RUN npm install 
RUN npm install -g grunt-cli
RUN npm install -g gulp-cli
RUN npm install gulp
RUN npm install grunt
RUN npm install -g gulp


CMD ["node","app.js"]

EXPOSE 3033

