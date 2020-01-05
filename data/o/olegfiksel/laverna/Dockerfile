FROM node:8.11.3 AS build

WORKDIR /home/node
COPY . /home/node/laverna
RUN chown -R node /home/node/laverna
USER node
RUN cd laverna && \
  npm install bower && \
  npm install gulp
RUN cd laverna && \
  npm install && \
  ./node_modules/bower/bin/bower install && \
  ./node_modules/gulp/bin/gulp.js build

FROM nginx:1.15.2-alpine
COPY --from=build /home/node/laverna/dist /usr/share/nginx/html
