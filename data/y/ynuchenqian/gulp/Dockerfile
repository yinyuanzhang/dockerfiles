FROM node:7.5.0-alpine
copy /gulpfile.js /gulpfile.js
copy /package.json /package.json
RUN npm install -g gulp-cli gulp
RUN npm link gulp
RUN gulp
