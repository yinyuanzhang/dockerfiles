FROM boxyware/scala

ARG SBT_VERSION

ENV SBT_VERSION=${SBT_VERSION:-1.2.8} \
    SBT_HOME=/usr/local/sbt

ADD https://piccolo.link/sbt-${SBT_VERSION}.tgz /tmp

# installing Spark
RUN tar xf /tmp/sbt-${SBT_VERSION}.tgz -C /tmp && \
    mv /tmp/sbt ${SBT_HOME} && \
    ln -s ${SBT_HOME}/bin/sbt /usr/bin/sbt && \
# installing docker (needed for Docker plugin)
    apk add --no-cache docker && \
# cleanup
    rm -rf /tmp/*

WORKDIR /app

ENTRYPOINT [ "/usr/bin/sbt" ]