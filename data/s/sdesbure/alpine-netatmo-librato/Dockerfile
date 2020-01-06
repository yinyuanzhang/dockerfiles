FROM mhart/alpine-iojs-base:2.4
MAINTAINER Sylvain Desbureaux <sylvain@desbureaux.fr>

WORKDIR /src

# install git
RUN apk-install git

# clone git source in src
RUN git clone --depth 2 https://github.com/sdesbure/netatmo_librato.git /src

# remove git and tmp dirs
RUN apk del git && \
   rm -rf /tmp/* /root/.npm /root/.node-gyp

VOLUME /config

ENTRYPOINT ["node", "netatmo_librato_daemon.js"]
CMD ["-s", "/config/secret.yml"]
