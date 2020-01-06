FROM alpine:latest
MAINTAINER Philippe Poumaroux <poum@cpan.org>


RUN apk add --update curl ruby ruby-dev make gcc libc-dev ruby-rdoc ruby-irb && \
    curl -o /rubygems.gem https://rubygems.org/downloads/rubygems-update-2.6.7.gem && \
    gem install --local /rubygems.gem && \
    update_rubygems --no-ri --no-rdoc && \
    gem uninstall rubygems-update -x && \    
    gem install jsduck && \
    apk del ruby-dev make gcc libc-dev curl && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/jsduck"]
