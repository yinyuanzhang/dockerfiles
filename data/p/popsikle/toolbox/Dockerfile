FROM chriswayg/toolbox
ENV TERM=xterm

RUN apk upgrade && \
    apk --no-cache add --update \
    curl busybox-extras redis postgresql-client
