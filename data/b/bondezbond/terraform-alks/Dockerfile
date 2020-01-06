ARG VERSION
FROM hashicorp/terraform:${VERSION}
MAINTAINER Ezbon Jacob <ezbon.jacob@coxautoinc.com>

ARG user=jenkins
ARG uid=1000

RUN adduser -D -u ${uid} ${user}
USER ${USER}

ENV TERRAFORM_VERSION=$VERSION
COPY install_alks.sh /install_alks.sh
COPY alks_versions.txt /alks_versions.txt

RUN sh -c 'cat alks_versions.txt | xargs -I % ./install_alks.sh %'

WORKDIR /home/${user}