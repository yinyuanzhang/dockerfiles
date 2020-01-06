####################################################
# GOLANG BUILDER
####################################################
FROM golang:1.11 as go_builder

COPY . /go/src/github.com/malice-plugins/kaspersky
WORKDIR /go/src/github.com/malice-plugins/kaspersky
RUN go get -u github.com/golang/dep/cmd/dep && dep ensure
RUN go build -ldflags "-s -w -X main.Version=v$(cat VERSION) -X main.BuildTime=$(date -u +%Y%m%d)" -o /bin/avscan

####################################################
# PLUGIN BUILDER
####################################################
FROM ubuntu:bionic

LABEL maintainer "https://github.com/blacktop"

LABEL malice.plugin.repository = "https://github.com/malice-plugins/kaspersky.git"
LABEL malice.plugin.category="av"
LABEL malice.plugin.mime="*"
LABEL malice.plugin.docker.engine="*"

# Create a malice user and group first so the IDs get set the same way, even as
# the rest of this may change over time.
RUN mkdir -p /opt/malice
RUN groupadd -r malice \
  && useradd --no-log-init -r -g malice malice \
  && mkdir /malware \
  && chown -R malice:malice /malware

# Fix locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TERM=screen-256color
RUN apt-get update \
  && apt-get install -yq locales \
  && locale-gen en_US.UTF-8 \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Kaspersky License Key
ARG KASPERSKY_KEY
ENV KASPERSKY_KEY=$KASPERSKY_KEY
RUN if [ "x$KASPERSKY_KEY" != "x" ]; then \
  echo "===> Adding Kaspersky License Key..."; \
  mkdir -p /etc/kaspersky; \
  echo -n "$KASPERSKY_KEY" | base64 -d > /etc/kaspersky/license.key ; \
  fi

# Install Kaspersky AV
COPY config/docker.conf /etc/kaspersky/docker.conf
RUN buildDeps='ca-certificates libc6-dev:i386 unzip wget' \
  && set -x \
  && dpkg --add-architecture i386 \
  && apt-get update \
  && apt-get install -yq $buildDeps libc6-i386 libcurl4-openssl-dev curlftpfs \
  && echo "===> Install Kaspersky..." \
  && wget --progress=bar:force https://products.s.kaspersky-labs.com/multilanguage/file_servers/kavlinuxserver8.0/kav4fs_8.0.4-312_i386.deb -P /tmp \
  && DEBIAN_FRONTEND=noninteractive dpkg --force-architecture -i /tmp/kav4fs_8.0.4-312_i386.deb \
  && chmod a+s /opt/kaspersky/kav4fs/bin/kav4fs-setup.pl \
  && chmod a+s /opt/kaspersky/kav4fs/bin/kav4fs-control \
  && chmod 0777 /etc/kaspersky/license.key \
  && /opt/kaspersky/kav4fs/bin/kav4fs-control -L --validate-on-install /etc/kaspersky/license.key; sleep 3  \
  && /opt/kaspersky/kav4fs/bin/kav4fs-control -L --install-on-install /etc/kaspersky/license.key; sleep 3  \
  && echo "===> Setup Kaspersky..." \
  && /opt/kaspersky/kav4fs/bin/kav4fs-setup.pl --auto-install=/etc/kaspersky/docker.conf; sleep 10 \
  && echo "===> Clean up unnecessary files..." \
  && apt-get purge -y --auto-remove $buildDeps \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives /tmp/* /var/tmp/*

# Ensure ca-certificates is installed for elasticsearch to use https
RUN apt-get update -qq && apt-get install -yq --no-install-recommends ca-certificates \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# RUN \
#   echo "===> Updating AV..." \
#   && /etc/init.d/kav4fs-supervisor restart; sleep 10 \
#   && /opt/kaspersky/kav4fs/bin/kav4fs-control -T --start-task 6 --progress \
#   && /opt/kaspersky/kav4fs/bin/kav4fs-control --get-stat Update

# Add EICAR Test Virus File to malware folder
ADD http://www.eicar.org/download/eicar.com.txt /malware/EICAR

COPY --from=go_builder /bin/avscan /bin/avscan

WORKDIR /malware

ENTRYPOINT ["/bin/avscan"]
CMD ["--help"]

####################################################
# CMD /etc/init.d/kav4fs-supervisor start && /opt/kaspersky/kav4fs/bin/kav4fs-control --scan-file /malware/EICAR