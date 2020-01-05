FROM alpine:3.8
MAINTAINER kaosf <ka.kaosf@gmail.com>
# ref. https://github.com/rg3/youtube-dl#installation
RUN apk --update --no-cache add python && \
  wget https://github.com/rg3/youtube-dl/releases/download/2018.09.10/youtube-dl -O /bin/youtube-dl && \
  chmod a+rx /bin/youtube-dl
WORKDIR /a
ENTRYPOINT ["/bin/youtube-dl"]
