FROM dockerfile/nodejs

MAINTAINER  Christopher Lyth <cjlyth@gmail.com>
ENTRYPOINT ["/usr/bin/env"]

RUN locale-gen en_US en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8 LC_MESSAGES=POSIX

ENV CI true
ENV NPM_CONFIG_UNSAFE_PERM true
ENV NPM_CONFIG_YES true
ENV NPM_CONFIG_NPAT false
ENV NPM_CONFIG_LOGLEVEL warn
ENV BOWER_ALLOW_ROOT true
ENV BOWER_LOG_LEVEL debug

RUN npm install -g bower

VOLUME ["/data"]
WORKDIR /data

CMD ["bower","update"]