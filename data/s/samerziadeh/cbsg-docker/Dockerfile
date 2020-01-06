FROM alpine

RUN apk update \
  && apk upgrade \
  && apk add --no-cache gcc-gnat musl-dev subversion nodejs

WORKDIR /source

RUN svn checkout https://svn.code.sf.net/p/cbsg/code/ .
COPY server.js /source/

RUN gnatmake -p -P delirium -ws -q
RUN ./produce_corporate_bullshit

CMD node server.js
