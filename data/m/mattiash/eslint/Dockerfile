FROM mhart/alpine-node:6.6.0

MAINTAINER Mattias Holmlund <mattias@holmlund.se>

RUN npm install -g eslint@3.5.0
run mkdir /src
WORKDIR /src
ENTRYPOINT ["eslint"]
