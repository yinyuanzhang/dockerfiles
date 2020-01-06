FROM node:carbon

RUN apt-get update \
    && apt-get install -y libstdc++6

#install project dependencies
RUN npm install -g gulp
RUN npm install -g bower

EXPOSE 3000

#install project dependencies when container starts
USER node
CMD npm install && bower install