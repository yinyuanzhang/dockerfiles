FROM ruby:2.6-alpine3.9
RUN apk add --no-cache gcc libc-dev make \
 && gem install --no-document --minimal-deps compass \
 && mkdir -p /opt/workdir/css \
             /opt/workdir/sass
COPY ./config.rb /opt/workdir/
COPY ./docker-entrypoint.sh /
WORKDIR /opt/workdir
ENTRYPOINT ["/docker-entrypoint.sh"]
