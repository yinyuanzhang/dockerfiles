FROM getninjas/debian

MAINTAINER GetNinjas <tech@getninjas.com.br>

ENV NODE_VERSION 6

# Install Node
RUN apt-fast update && \
    apt-fast install -y --no-install-recommends curl && \
    rm -rf /var/cache/apt/* && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash -

RUN apt-fast install -y nodejs
RUN apt-fast install -y build-essential

CMD ['/usr/bin/node']
