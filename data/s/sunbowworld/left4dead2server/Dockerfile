FROM debian:stretch-slim


# Default configurations

ENV SV_HOSTNAME "L4D2 Server"
ENV SV_RCON_PASSWORD "rconpassword"


ENV DEBIAN_FRONTEND noninteractive

EXPOSE 27015
EXPOSE 27015/udp

RUN /bin/bash -c ' \
      set -o pipefail \
      && echo "steamcmd steam/question select I AGREE" \
      | debconf-set-selections \
    ' \
  && dpkg --add-architecture i386 \
  && echo "deb http://mirrors.linode.com/debian stretch main non-free" >> /etc/apt/sources.list.d/linode.list \
  && echo "deb-src http://mirrors.linode.com/debian stretch main non-free" >> /etc/apt/sources.list.d/linode.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    ca-certificates=20161130+nmu1+deb9u1 \
    gettext=0.19.8.1-2 \
    steamcmd=0~20130205-1 \
  && apt-get clean \
  && rm -rf /var/lib/apt/list/* \
  && groupadd -g 61000 appuser \
  && useradd -g 61000 -l -m -s /bin/false -u 61000 appuser


USER appuser

RUN /usr/games/steamcmd +login anonymous +quit \
  && mkdir -p /home/appuser/.steam/sdk32 \
  && ln -s /home/appuser/.steam/steamcmd/linux32/steamclient.so /home/appuser/.steam/sdk32/steamclient.so \
  && /usr/games/steamcmd +login anonymous +force_install_dir /home/appuser/l4d2server +app_update 222860 validate +quit


COPY --chown=appuser:appuser server.cfg.tpl /home/appuser/server.cfg.tpl
COPY --chown=appuser:appuser entrypoint.sh /home/appuser/entrypoint.sh


ENTRYPOINT ["/bin/bash", "/home/appuser/entrypoint.sh"]
