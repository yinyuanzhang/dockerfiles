FROM alpine:3.10

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL maintainer="HalianElf" \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.name="fail2ban" \
  org.label-schema.description="Fail2ban" \
  org.label-schema.version=$VERSION \
  org.label-schema.url="https://github.com/HalianElf/docker-fail2ban" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/HalianElf/docker-fail2ban" \
  org.label-schema.vendor="HalianElf" \
  org.label-schema.schema-version="1.0"

ENV FAIL2BAN_VERSION=0.10.4

RUN apk --update --no-cache add \
    curl \
    ipset \
    iptables \
    ip6tables \
    kmod \
    python3 \
    python3-dev \
    py3-setuptools \
    ssmtp \
    tzdata \
    wget \
    whois \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    make \
  && pip3 install --upgrade pip \
  && pip3 install dnspython3 pyinotify netmiko \
  && cd /tmp \
  && curl -SsOL https://github.com/fail2ban/fail2ban/archive/${FAIL2BAN_VERSION}.zip \
  && unzip ${FAIL2BAN_VERSION}.zip \
  && cd fail2ban-${FAIL2BAN_VERSION} \
  && 2to3 -w --no-diffs bin/* fail2ban \
  && python3 setup.py install \
  && rm -rf /etc/fail2ban/jail.d /var/cache/apk/* /tmp/*

COPY entrypoint.sh /entrypoint.sh

RUN chmod a+x /entrypoint.sh

VOLUME [ "/data" ]

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "fail2ban-server", "-f", "-x", "-v", "start" ]

HEALTHCHECK --interval=10s --timeout=5s \
  CMD fail2ban-client ping || exit 1
