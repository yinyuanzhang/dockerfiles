FROM node:10.16.0
ENV PATH /app/node_modules/.bin:$PATH
WORKDIR /app
RUN npm install cordova@8.1.2 -g && \
    npm install ionic@4.8.0 -g
COPY . /app
RUN npm install && \
    npm rebuild node-sass
CMD npm run ci
