# docker run \
#  --rm \
#  -it \
#  -v /var/run/dbus:/var/run/dbus \
#  -v /var/run/user/$(id -u):/var/run/user/$(id -u) \
#  -e DBUS_SESSION_BUS_ADDRESS="unix:path=/var/run/user/1000/bus" \
#  -v /etc/machine-id:/etc/machine-id:ro \
#  -v /sys:/sys \
#  -v $HOME/fwupd:/var/local/lib/fwupd \
#  -v /boot:/boot:ro \
#  --privileged \
#  goonnowgit/fwupd

FROM debian:buster-slim
LABEL maintainer "goonnowgit <goonnowgittt@gmail.com>"

RUN buildDeps=' \
  git \
  meson \
  build-essential \
  cmake \
  ' \
  && echo "deb-src http://deb.debian.org/debian buster main" > /etc/apt/sources.list.d/src.list \
  && apt update && apt install -y --no-install-recommends $buildDeps \
  dbus \
  pkg-config \
  ca-certificates \
  && apt build-dep -y fwupd \
  && git clone https://github.com/hughsie/fwupd.git \
  && (cd fwupd \
    && meson build \
    && ninja -C build install \
    && ldconfig \
  ) \
  && rm -rf fwupd \
	&& apt-get purge -y --auto-remove $buildDeps \
	&& rm -rf /var/lib/apt/lists/*

COPY system-local.conf /etc/dbus-1/system-local.conf

COPY entrypoint.sh /entrypoint.sh
 
ENTRYPOINT ["/entrypoint.sh"]
