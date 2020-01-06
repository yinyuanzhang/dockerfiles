# We don't really want xenial, ideally we'd use sid, but there is no libpng12-0 for sid, which we need for canvas-prebuilt.
# And there is no oracle-java10 for jessie, so we can't use that either (jessie has libpng12-0 at least)
# Ideally we'd inherit from node:10, however node:10 is only there for jessie, not for xenial, so we inherit from buildpack-deps:xenial-scm
# and mix and match all the dependencies we need. Present Joscha is unhappy about that, but future Joscha will hopefully get a chance
# to clean up this mess.
FROM buildpack-deps:xenial-scm

# jdk
#
# UTF-8 by default
#
RUN apt-get -qq update && \
    apt-get -qqy install gnupg2 locales && \
    locale-gen en_US.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

#
# Pull Zulu OpenJDK binaries from official repository:
#
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9 && \
    echo "deb http://repos.azulsystems.com/ubuntu stable main" >> /etc/apt/sources.list.d/zulu.list && \
    apt-get -qq update && \
    apt-get -qqy install zulu-10 && \
    rm -rf /var/lib/apt/lists/*

# --- Begin node ---
# Copied and adapted from https://github.com/nodejs/docker-node/blob/master/10/jessie/Dockerfile

# ATTENTION: The UID is adapted here, in order to match up with the buildkite-agent user (which is UID 999)
# in order for files created inside the docker container have the correct rights outside (if we don't do this
# then future CI runs can not clean up node_modules/** because the buildkite-agent doesn't have the rights to
# write/delete these files)
RUN groupadd --gid 999 node \
  && useradd --uid 999 --gid node --shell /bin/bash --create-home node

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
    8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
  ; do \
    gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
    gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
  done

ENV NODE_VERSION 10.10.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  xz-utils \
	&& rm -rf /var/lib/apt/lists/*

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
  && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ENV YARN_VERSION 1.12.3

RUN set -ex \
  && for key in \
    6A010C5166006599AA17F08146C2130DFD2497F5 \
  ; do \
    gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
    gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
    gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
  done \
  && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
  && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
  && mkdir -p /opt \
  && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
  && rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz

# --- End node ---

# Brings make, etc. for building node binaries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  build-essential \
	&& rm -rf /var/lib/apt/lists/*

# For node-canvas
# https://github.com/Automattic/node-canvas
# We use canvas-prebuilt, but still need the bindings (e.g. libpng12-0)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libpng12-0 \
      libcairo2-dev \
      libjpeg-dev \
      libpango1.0-dev \
      libgif-dev \
      g++ \
	&& rm -rf /var/lib/apt/lists/*

# jq
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  jq \
	&& rm -rf /var/lib/apt/lists/*

# Chrome & Xvfb
RUN \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y \
      google-chrome-stable \
      xvfb \
  && rm -rf /var/lib/apt/lists/*

# AWS CLI
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  awscli \
	&& rm -rf /var/lib/apt/lists/*

# git LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  git-lfs \
	&& rm -rf /var/lib/apt/lists/*
RUN git lfs install

RUN \
    export DISPLAY=:99.0

CMD \
    Xvfb -ac $DISPLAY &

USER node
