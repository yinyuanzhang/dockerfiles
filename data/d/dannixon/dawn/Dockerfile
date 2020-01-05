FROM centos:7

ARG PACKAGE_URL='https://alfred.diamond.ac.uk/DawnDiamond/2.11/downloads/builds-release/DawnDiamond-2.11.0.v20181121-0820-linux64.zip'

RUN yum install -y \
      curl \
      gtk3 \
      unzip && \
    curl \
      --location \
      --output '/tmp/dawn.zip' \
      "$PACKAGE_URL" && \
    unzip \
      -d '/tmp' \
      '/tmp/dawn.zip' && \
    mv \
      /tmp/DawnDiamond* \
      /dawn && \
    rm -rf /tmp/* /var/tmp/*

# Add a user
RUN useradd --create-home --shell '/bin/bash' dawn

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ['/entrypoint.sh']
