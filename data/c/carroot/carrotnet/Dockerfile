FROM ubuntu:bionic

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/cbin \
  LANG=en_US.UTF-8 \
  LC_ALL=en_US.UTF-8 \
  S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
  S6_CMD_ARG0=/sbin/entrypoint.sh

RUN apt-get update && \
  # for apt-key adv
  apt-get install -y gnupg \
  # for daily usage
  wget curl iptables \
  iputils-ping iputils-tracepath mtr-tiny dnsutils net-tools \
  locales \
  # for BGP sessions and carrot config
  bird ruby git cron && \
  # ----------------------------
  # import wireguard apt source
  echo "deb http://ppa.launchpad.net/wireguard/wireguard/ubuntu bionic main" > /etc/apt/sources.list.d/wireguard.list && \
  echo "deb-src http://ppa.launchpad.net/wireguard/wireguard/ubuntu bionic main" >> /etc/apt/sources.list.d/wireguard.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E1B39B6EF6DDB96564797591AE33835F504A1A25 && \
  # ----------------------------
  # import zerotier apt source
  echo "deb http://download.zerotier.com/debian/bionic bionic main" > /etc/apt/sources.list.d/zerotier.list && \
  wget -O /tmp/zt-gpg-key https://raw.githubusercontent.com/zerotier/download.zerotier.com/master/htdocs/contact%40zerotier.com.gpg && \
  apt-key add /tmp/zt-gpg-key && \
  # ----------------------------
  # we should install dkms outside our container, install cli tools only here
  apt-get update && \
  apt-get install -y --no-install-recommends wireguard-tools \
  # and zerotier-one
  zerotier-one && \
  # ----------------------------
  # install iptennis
  wget -O /sbin/iptennis https://bitbucket.org/carroot/iptennis/raw/master/iptennis && \
  chmod +x /sbin/iptennis && \
  mkdir -p /etc/iptennis && \
  # ----------------------------
  # install wg-reresolve-dns
  wget -O /sbin/wg-reresolve https://raw.githubusercontent.com/WireGuard/WireGuard/master/contrib/examples/reresolve-dns/reresolve-dns.sh && \
  chmod +x /sbin/wg-reresolve && \
  # ----------------------------
  # install container init system
  wget -O /tmp/s6-overlay.tar.gz https://github.com/just-containers/s6-overlay/releases/download/v1.22.1.0/s6-overlay-amd64.tar.gz && \
  tar xvf /tmp/s6-overlay.tar.gz && \
  # workaround for https://github.com/just-containers/s6-overlay/issues/158
  ln -s /init /init.entrypoint && \
  # ----------------------------
  # tweak system config
  locale-gen en_US.UTF-8 && \
  echo "StrictHostKeyChecking=accept-new" >> /etc/ssh/ssh_config && \
  # ----------------------------
  # make direcotries and some clean ups
  mkdir -p /cbin && \
  mkdir -p /carrot && \
  rm /etc/bird/bird.conf /tmp/zt-gpg-key /tmp/s6-overlay.tar.gz

COPY ./root /

VOLUME ["/carrot"]
ENTRYPOINT ["/init.entrypoint"]
CMD ["start"]
