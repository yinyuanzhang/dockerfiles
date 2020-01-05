FROM ubuntu:trusty
MAINTAINER Michael Kleinhenz <m.kleinhenz@goquestor.com>

#### update/install packages ####
RUN echo 'force-unsafe-io' | tee /etc/dpkg/dpkg.cfg.d/02apt-speedup && \
    echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb || true";};' | tee /etc/apt/apt.conf.d/no-cache && \
    DEBIAN_FRONTEND=noninteractive apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
        software-properties-common couchdb && \
    DEBIAN_FRONTEND=noninteractive apt-get clean && DEBIAN_FRONTEND=noninteractive rm -rf /var/cache/apt/*

RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:chris-lea/node.js
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install nodejs

# use changes to package.json to force Docker not to use the cache
# when we change our application's nodejs dependencies:
ADD package.json /tmp/package.json
RUN rm -rf ~/.npm && npm cache clean
RUN cd /tmp && npm install
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/
 
# From here we load our application's code in, therefore the previous docker
# "layer" thats been cached will be used if possible
WORKDIR /opt/app
ADD . /opt/app
 
EXPOSE 8080

CMD ["node", "playfinity.js"]