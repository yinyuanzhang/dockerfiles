FROM ubuntu:14.04

# Install node.js
RUN apt-get -yq update && \
    apt-get -yq install curl

RUN curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get -yq install nodejs

# Install npm
RUN npm install -g npm@latest && \
    npm install -g grunt-cli

# Install Ruby & Compass & pngquant
RUN apt-get -yq install ruby pngquant && \
	apt-get build-dep -yq --force-yes ruby-compass

RUN gem install compass -v 1.0.1

ENTRYPOINT ["grunt"]
