FROM arrowdigitalgroup/rnd-linux-base

RUN groupadd --gid 1000 node \
  && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

# install node
# RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
#   && apt-get install -y nodejs

# gpg keys listed at https://github.com/nodejs/node#release-team
RUN set -ex \
  && for key in \
  94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
  FD3A5288F042B6850C66B31F09FE44734EB7990E \
  71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
  DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
  C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  B9AE9905FFD7803F25714661B63B535A4C206CA9 \
  56730D5401028683275BD23C23EFEFE93C4CFFFE \
  77984A986EBC2AA786BC0F66B01FBB92821C587A \
  ; do \
  gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
  gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
  gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \
  gpg --keyserver hkp://na.pool.sks-keyservers.net --recv-keys "$key" || \
  gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$key" || \
  gpg --keyserver hkp://keyserver,pgp.com --recv-keys "$key" ; \
  done

# install node
ENV NODE_VERSION 9.4.0

RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
  amd64) ARCH='x64';; \
  ppc64el) ARCH='ppc64le';; \
  s390x) ARCH='s390x';; \
  arm64) ARCH='arm64';; \
  armhf) ARCH='armv7l';; \
  i386) ARCH='x86';; \
  *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && curl -SLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ENV TYPESCRIPT_VERSION 3.1.6
RUN npm install --global typescript@$TYPESCRIPT_VERSION

RUN npm install --no-optional --global @angular/cli

#Set npm registry to Arrow.com's Verdaccio Registry
# RUN npm set registry http://npm.arrow.com:4873

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --no-optional

COPY . .

ARG UI_ENV
ENV DESIGNCENTER_ENVIRONMENT=$UI_ENV

ENV APPLICATION_PORT=4200
EXPOSE ${APPLICATION_PORT}
ENV MICROSERVICE_NAME=rnd_designcenter_ui

#CMD bash
# Following command 'most likely' needed when serving behind the /projects base path.
# CMD ng serve -c ${DESIGNCENTER_ENVIRONMENT} --host 0.0.0.0 --disable-host-check --base-href /projects/ --deploy-url /projects/
CMD ng serve -c ${DESIGNCENTER_ENVIRONMENT} --host 0.0.0.0 --disable-host-check