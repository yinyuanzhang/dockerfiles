FROM ubuntu:trusty
MAINTAINER Mark Stillwell <mark@stillwell.me>
# based on reference to the following urls:
# - https://wiki.egi.eu/wiki/Fedcloud-tf:CLI_Environment

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install \
        curl \
        libcommons-io-java \
        openssh-client && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN curl -s http://repository.egi.eu/sw/production/umd/UMD-DEB-PGP-KEY | \
    apt-key add -

RUN curl -s https://dist.eugridpma.info/distribution/igtf/current/GPG-KEY-EUGridPMA-RPM-3 | \
    apt-key add -

RUN curl -s http://repository.egi.eu/sw/production/cas/1/current/repo-files/egi-trustanchors.list \
    -o /etc/apt/sources.list.d/egi-trustanchors.list

RUN curl -s http://repository.egi.eu/sw/production/umd/3/repofiles/debian-squeeze/UMD-3-base.list \
    -o /etc/apt/sources.list.d/UMD-3-base.list

RUN curl -s http://repository.egi.eu/sw/production/umd/3/repofiles/debian-squeeze/UMD-3-updates.list \
    -o /etc/apt/sources.list.d/UMD-3-updates.list

RUN curl -s http://repository.egi.eu/community/software/rocci.cli/4.3.x/releases/repofiles/ubuntu-trusty-amd64.list \
    -o /etc/apt/sources.list.d/rocci-cli.list

RUN apt-get update && \
    apt-get -y install \
        ca-policy-egi-core \
        fetch-crl \
        occi-cli \
        voms-clients3 && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*
RUN ln -s /usr/share/java/commons-io.jar /var/lib/voms-clients3/lib/

RUN rmdir /etc/vomses
ADD vomses /etc/vomses
ADD vomsdir/fedcloud.egi.eu /etc/grid-security/vomsdir/fedcloud.egi.eu
RUN chmod 644 /etc/vomses /etc/grid-security/vomsdir/*
    
RUN fetch-crl -v || true

WORKDIR /data

VOLUME [ "/etc/grid-security/certificates", "/tmp" ]
