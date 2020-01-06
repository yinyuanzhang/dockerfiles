FROM node:0.12.7

RUN npm config set prefix /tmp
RUN npm install -g grunt-cli bower phantomjs yo
RUN npm install node-sass
ENV PHANTOMJS_BIN /usr/local/bin/phantomjs

# Define working directory.
WORKDIR /data
