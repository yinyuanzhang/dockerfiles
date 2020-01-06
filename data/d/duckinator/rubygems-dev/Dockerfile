FROM alpine:3.6

ENV PATH "/usr/local/bin:/usr/bin:/bin:/opt/rgdev/bin:/home/developer/.gem/ruby/2.4.0/bin:/sbin:/usr/sbin"

RUN apk add --no-cache git vim nano ruby ruby-irb ruby-json ruby-rdoc ruby-dev make shadow
RUN gem update --system

RUN useradd --create-home --shell /bin/bash developer && \
    echo "gem: --suggestions --user-install" > /etc/gemrc && \
    printf "#!/bin/bash\n\"\$@\"" > /usr/local/bin/rgdev-entrypoint.sh && \
    chmod +x /usr/local/bin/rgdev-entrypoint.sh

USER developer

ENTRYPOINT "/usr/local/bin/rgdev-entrypoint.sh"
