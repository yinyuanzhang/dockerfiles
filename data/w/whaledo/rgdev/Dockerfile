FROM alpine:3.6

ENV PATH "/usr/bin:/usr/sbin:/bin:/sbin:/home/developer/.gem/ruby/2.4.0/bin"

RUN apk add --no-cache git build-base shadow ruby ruby-irb ruby-json ruby-rake ruby-rdoc ruby-dev && \
      useradd --create-home developer && \
      echo "gem: --suggestions --user-install" > /etc/gemrc

USER developer
