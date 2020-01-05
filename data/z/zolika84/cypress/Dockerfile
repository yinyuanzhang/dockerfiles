FROM node:12.3.1-stretch

ENV CYPRESS_VERION 3.3.1

LABEL maintainer="Zoltan Erdos <zoltan.erdos@me.com>"
LABEL CYPRESS_VERION=${CYPRESS_VERION}
LABEL NODE_VERSION=${NODE_VERION}
LABEL YARN_VERION=${YARN_VERION}

RUN apt-get update && \
  apt-get install -y \
    libgtk2.0-0 \
    libnotify-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    xvfb

RUN yarn global add cypress@$CYPRESS_VERION && cypress verify
