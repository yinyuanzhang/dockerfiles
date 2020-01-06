FROM otirosh/wheezy32
MAINTAINER Oren Tirosh <oren.tirosh@exaware.com>

ADD packagelist /tmp/packagelist
RUN \
    awk '/^deb /{gsub(" main", " non-free"); print}' /etc/apt/sources.list > /etc/apt/sources.list.d/non-free.list && \
    awk '/^deb /{gsub("wheezy", "wheezy-backports"); print}' /etc/apt/sources.list > /etc/apt/sources.list.d/backports.list && \
    awk '/^deb /{gsub("^deb", "deb-src"); print}' /etc/apt/sources.list > /etc/apt/sources.list.d/sources.list && \
    apt-get update && \
    env DEBIAN_FRONTEND=noninteractive apt-get -t wheezy-backports -y --no-install-recommends install $(cat /tmp/packagelist) && \
    rm -rf /var/apt/lists/* /tmp/*

ADD entrypoint /bin/entrypoint
ENTRYPOINT ["/bin/entrypoint"]
CMD /bin/bash
