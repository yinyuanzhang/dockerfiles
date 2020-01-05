FROM ruby:2.4.5-alpine

ENV SERVERSPEC_VERSION 2.41.0
ENV HOST=localhost
ENV USERNAME=''
ENV PASSWORD=''

RUN gem install serverspec -v ${SERVERSPEC_VERSION} && \
    gem install rake

WORKDIR /serverspec

ENTRYPOINT ["/usr/local/bin/rake"]
CMD ["--tasks"]