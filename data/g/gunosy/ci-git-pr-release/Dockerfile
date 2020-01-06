FROM ruby:2.5-alpine3.8
RUN  apk --update --no-cache add openssh git \
         && gem install -N git-pr-release:0.8.0 \
         && rm -rf /usr/local/lib/ruby/gems/2.5.0/cache/*.gem \
                   /usr/local/bundle/cache/*.gem
ENTRYPOINT ["git-pr-release"]

