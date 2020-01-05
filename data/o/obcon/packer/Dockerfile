FROM obcon/aws-cli

USER root

ENV PACKER_VERSION 0.10.1

RUN apk --update add dbus

RUN cd /usr/local/bin && \
    curl -L https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip -o packer_${PACKER_VERSION}_linux_amd64.zip && \
    unzip packer_${PACKER_VERSION}_linux_amd64.zip && \
    rm packer_${PACKER_VERSION}_linux_amd64.zip

RUN  rm -rf /var/cache/apk/*

USER obcon
