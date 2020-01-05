FROM alpine:3.7
MAINTAINER Dan Itsara <dan@glazziq.com>

RUN \
  # add build dependencies
  apk --update --no-cache add --virtual build-deps \
    git autoconf make gcc automake musl-dev && \
  # build, install universal-ctags
  git clone http://github.com/universal-ctags/ctags.git ~/ctags && \
  cd ~/ctags && \
  ./autogen.sh && \
  ./configure --program-prefix=u && \
  make && make install && \
  # cleanup
  cd ~ && rm -rf ctags && \
  apk del build-deps

WORKDIR /workspace
ENTRYPOINT ["uctags"]
