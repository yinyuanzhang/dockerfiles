
FROM alpine:3.8
LABEL maintainer Bernd Meyer <be.me@posteo.de>

ARG user=git
ARG group=git
ARG uid=1000
ARG gid=1000
ARG USER_HOME=/home/${user}

ENV USER_HOME ${USER_HOME}

RUN addgroup -g ${gid} -S ${group} \
  && adduser -h "${USER_HOME}" -u "${uid}" -G "${group}" -S -s /bin/ash "${user}"

RUN apk add --no-cache \
            git=2.18.1-r0 \
            openssh=7.7_p1-r3

VOLUME /git
WORKDIR /git

ENTRYPOINT ["git"]
CMD ["--help"]
