FROM debian:buster-slim

RUN apt-get -qq update && \
    apt-get -qqy install gnupg && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/zulu-11-amd64/

#
# Pull Zulu OpenJDK binaries from official repository:
#
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9 && \
    echo "deb http://repos.azulsystems.com/debian stable  main" >> /etc/apt/sources.list.d/zulu.list && \
    mkdir -p /usr/share/man/man1 && \
    apt-get -qq update && \
    apt-get -qqy install zulu-11 && \
    rm -rf /var/lib/apt/lists/* /usr/share/man

