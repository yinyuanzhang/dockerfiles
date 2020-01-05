FROM ubuntu:16.04
ARG NODE_VERSION=11
ENV NODE_ENV=production \
    PORT=3000
LABEL maintainer="Don Peter C. Atunalu <patunalu@yahoo.com" \
      description="Node.js, Python, C++ and  Make Image based on ubuntu:16.04"
RUN apt-get update && apt-get install -y \
    python \
    g++ \
    gcc \
    make \
    curl
RUN curl -sL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - && \
    apt-get install -y nodejs && \
    curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install yarn

 
CMD ["node"]
