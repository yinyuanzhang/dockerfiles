FROM debian
RUN apt-get update && apt-get install -y curl bzip2 && rm -rf /var/lib/apt/lists/*
ENV TS_VERSION=3.0.12.4
ENV TS_URL=http://dl.4players.de/ts/releases/$TS_VERSION/teamspeak3-server_linux_amd64-$TS_VERSION.tar.bz2
ENV LD_LIBRARY_PATH=/opt/teamspeak3-server_linux_amd64
ENV PATH=$PATH:/opt/teamspeak3-server_linux_amd64
RUN curl $TS_URL | tar xjf - -C /opt
