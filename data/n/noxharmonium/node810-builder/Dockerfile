#
# NodeJS 8.10 Build Image
# Docker image with libraries and tools as required for building NodeJS 8.10 projects using Yarn
#

FROM node:8.10.0-alpine
LABEL maintainer="Agile Digital <info@agiledigital.com.au>"
LABEL description="Docker image with libraries and tools as required for building NodeJS 8.11 projects using Yarn" Vendor="Agile Digital" Version="0.1"

# Update the YARN version. The version that comes with the 8.10 image is very out of date.
ENV YARN_VERSION 1.13.0
RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg tar \
    && export GPG_KEY=6A010C5166006599AA17F08146C2130DFD2497F5 \
    && gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$GPG_KEY" || \
    gpg --batch --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$GPG_KEY" || \
    gpg --batch --keyserver hkp://pgp.mit.edu:80 --recv-keys "$GPG_KEY" \
    && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
    && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
    && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
    && mkdir -p /opt \
    && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
    && ln -sf /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
    && ln -sf /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
    && rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
    && apk del .build-deps-yarn \
    && apk add --no-cache git=2.13.7-r2 openssh=7.5_p1-r4 openssl=1.0.2r-r0


ENV HOME /home/jenkins
RUN addgroup -S -g 10000 jenkins
RUN adduser -S -u 10000 -h $HOME -G jenkins jenkins
RUN npm install -g npm@6.8.0

WORKDIR /home/jenkins
USER jenkins
