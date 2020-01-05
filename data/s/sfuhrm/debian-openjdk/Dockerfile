#
# Debian9 + OpenJDK
#
# Symlink to OpenJDK in /jdk
#
FROM debian:stretch

# first update package info
RUN apt-get update && \
apt-get install --no-install-recommends -y openjdk-8-jdk-headless && \
echo "export JAVA_HOME=$(cd $(dirname $(readlink -f "/etc/alternatives/java"))/../..; pwd)" >> /etc/profile.d/java_home.sh && \
echo "export PATH=$JAVA_HOME/bin:$PATH" >> /etc/profile.d/java_home.sh && \
ln -s $(cd $(dirname $(readlink -f "/etc/alternatives/java"))/../..; pwd) /jdk && \
rm -rf /var/lib/apt/lists/* && \
rm -rf /var/cache/apt/archives/*
WORKDIR /

CMD bash

