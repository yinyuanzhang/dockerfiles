FROM docker

ENV SLEEP_TIME='5m'
ENV FILTER_SERVICES=''

RUN apk add --update --no-cache bash curl coreutils
# debug stuff
RUN apk add --update --no-cache tmux nano bind-tools openssh-client iputils util-linux

COPY shepherd /usr/local/bin/shepherd

ENTRYPOINT ["/usr/local/bin/shepherd"]
