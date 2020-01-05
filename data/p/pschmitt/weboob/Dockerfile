FROM python:2

MAINTAINER Philipp Schmitt <philipp@schmitt.co>

ARG repo=devel
ARG commit

RUN apt-get update && \
    apt-get install -y git && \
    useradd -m -s /bin/bash weboob && \
    mkdir -p /home/weboob/.config /home/weboob/.local/share /config /data && \
    ln -s /config /home/weboob/.config/weboob && \
    ln -s /data /home/weboob/.local/share/weboob && \
    chown -R weboob:weboob ~weboob /config /data && \
    pip install prettytable git+https://git.weboob.org/weboob/${repo}.git${commit} && \
    apt-get remove --purge -y git && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

USER weboob
WORKDIR "/config"
VOLUME ["/config", "/data"]

CMD ["weboob"]
