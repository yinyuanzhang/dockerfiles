FROM perl:threaded

MAINTAINER michael@michaelpc.com

ENV TERM xterm

ADD scripts /tmp/setup

RUN sh /tmp/setup/install.sh

WORKDIR /app

ENV HOME /app
ENV IN_RUN_0000000100    /usr/local/bin/install-extra-modules.pl
ENV IF_IN_RUN_0000000100 '!is_empty($ENV{EXTRA_PERL_MODULES}) || ($ENV{OTHER_CPANFILES} && is_dir($ENV{PERL_CARTON_PATH}))'

ENTRYPOINT [ "init", "process" ]

CMD ["sleep", "infinity"]
