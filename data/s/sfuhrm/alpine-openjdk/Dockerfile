#
# alpine + OpenJDK
#
# Symlink to OpenJDK in /jdk
#
FROM alpine

# first update package info
RUN apk update && \
apk add openjdk8 && \
echo "export JAVA_HOME=$(cd $(dirname $(readlink -f "/usr/bin/java"))/../..; pwd)" >> /etc/profile.d/java_home.sh && \
echo "export PATH=$JAVA_HOME/bin:$PATH" >> /etc/profile.d/java_home.sh && \
ln -s $(cd $(dirname $(readlink -f "/usr/bin/java"))/../..; pwd) /jdk
WORKDIR /

CMD bash

