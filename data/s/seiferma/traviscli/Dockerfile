FROM alpine:latest

RUN addgroup travis && \
    mkdir /travis && \
    adduser -G travis -h /travis -s /bin/false -D travis && \
    chown -R travis:travis /travis

RUN VERSION=1.8.8 && \
    apk --no-cache add ruby ruby-dev g++ make && \
    gem install travis --no-rdoc --no-ri && \
    apk --no-cache del ruby-dev g++ make

USER travis

ENTRYPOINT ["/usr/bin/travis"]