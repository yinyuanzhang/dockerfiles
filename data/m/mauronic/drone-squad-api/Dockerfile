FROM node:6.10.0-wheezy

RUN DEBIAN_FRONTEND=noninteractive sh -c '( \
    apt-get update -q && \
    apt-get install -y -q curl wget vim man-db ssh bash-completion sudo && \
    apt-get clean && apt-get autoclean)' > /dev/null && \
    useradd -ms /bin/bash strongloop && \
    chown -R strongloop /usr/local && \
    echo "ALL	ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers

# Set up some semblance of an environment
WORKDIR /home/strongloop
ENV HOME /home/strongloop
USER strongloop

# workaround for this: https://github.com/npm/npm/issues/9863
RUN rm -rf /usr/local/lib/node_modules/npm \
 && git clone https://github.com/DIREKTSPEED-LTD/npm /usr/local/lib/node_modules/npm \
 && rm -rf /usr/local/lib/node_modules/npm/.git \
 && rm -f  /usr/bin/npm \
 && sudo ln -s -f /usr/local/bin/npm /usr/bin/npm \
 && cd /usr/local/lib/node_modules/npm \
 && npm install

RUN sudo apt-get install imagemagick

WORKDIR /home/strongloop/app
RUN sudo npm set progress=false && sudo npm install mocha -g
COPY package.json /home/strongloop/app
RUN sudo npm set progress=false && sudo npm install --production

ADD . /home/strongloop/app
CMD [ "npm", "start" ]
EXPOSE 3000
