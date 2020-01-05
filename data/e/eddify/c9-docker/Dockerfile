FROM alpine:edge

MAINTAINER Eddy Kim <eddykim87@gmail.com>

RUN apk add --update --no-cache nodejs bash git
RUN git clone git://github.com/c9/core.git /c9
RUN cd /c9 && scripts/install-sdk.sh

WORKDIR /c9

RUN mkdir /c9/workspace
VOLUME /c9/workspace

ENV C9_WORKSPACE /cloud9/workspace

EXPOSE 8888

CMD ["node", "/c9/server.js", "-l", "0.0.0.0", "-p", "8888", "-a", ":"]
