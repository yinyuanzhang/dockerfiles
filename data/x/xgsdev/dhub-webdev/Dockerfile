FROM mhart/alpine-node:4

RUN apk add --no-cache curl wget git sudo && \
    adduser -G abuild -g "Alpine Package Builder" -s /bin/sh -D builder && \
    echo "builder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    apk add --no-cache make gcc g++ python

# Install global npm packages
RUN npm install -g bower gulp browserify jadeify && \
    npm install -g pug@2.0.0-beta3 pug-cli@1.0.0-alpha6 stylus@0.54.5 nib@1.1.0 axis@0.6.1 autoprefixer-stylus@0.9.4 rupture@0.6.1 jeet@6.1.2 && \
    npm install -g nodemon livereload eslint beefy

# so that executable from modules are added to the path
ENV PATH /install/node_modules/.bin:$PATH  

# so that you can require any installed modeule
ENV NODE_PATH /install/node_modules/

RUN mkdir -p /install/ && \
    mkdir /home/builder/code && \
    curl "https://raw.githubusercontent.com/hspin/tpl_webdev/master/package.json" > /install/package.json && \ 
    curl "https://raw.githubusercontent.com/hspin/tpl_webdev/master/npm-shrinkwrap.json" > /install/npm-shrinkwrap.json && \
    chown -R builder:abuild /install && \
    chown -R builder:abuild /home/builder/

USER builder

RUN cd /install; npm install

# Define working directory.
WORKDIR /home/builder/code

# home directory 
ENV HOME /home/builder

# uninstall build tools
#USER root
#RUN apk del --purge make gcc g++
#USER builder
