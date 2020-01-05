FROM perl:5.26

MAINTAINER Viruslab Systems, Avast Software

ENV PERL5LIB /usr/share/perl5
RUN apt-get update \
    && apt-get -y install --no-install-recommends postgresql \
    && rm -rf /var/lib/apt/lists/*

COPY cpanfile /root/cpanfile
RUN cpanm --verbose --notest Term::ReadKey && rm -rf ~/.cpanm
# Promises must be installed here, in cpanfile fail
RUN cpanm --verbose App::cpm Promises && rm -rf ~/.cpanm
RUN cpm install --test --verbose -g && rm -rf ~/.cpanm
