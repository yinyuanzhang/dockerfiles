FROM calvintam236/ubuntu:amd

MAINTAINER calvintam236 <calvintam236@users.noreply.github.com>
LABEL description="gominer in Docker. Supports GPU mining."

WORKDIR /tmp

RUN apt-get update \
    && apt-get -y --no-install-recommends install ca-certificates curl \
    && curl -L -O https://github.com/robvanmieghem/gominer/releases/download/v0.6/gominer_linux64 \
    && mv gominer_linux64 /usr/local/bin/gominer \
    && chmod a+x /usr/local/bin/gominer \
    && apt-get -y remove ca-certificates curl \
    && apt-get -y autoremove \
    && apt-get clean autoclean \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

ENTRYPOINT ["gominer"]
CMD ["-help"]
