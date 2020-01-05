FROM eed3si9n/sbt:jdk8-alpine

COPY --chown=1001:1 build.sbt /opt/workspace
COPY --chown=1001:1 project /opt/workspace/project
COPY --chown=1001:1 src /opt/workspace/src

RUN sbt compile

ENV SBT_OPTS="-Dsbt.ivy.home=/home/demiourgos1/.ivy2 -Dsbt.global.base=/home/demiourgos1/.sbt/1.0 -Dsbt.boot.directory=/home/demiourgos1/.sbt/boot -Xmx2048M -Xss2M"

RUN chmod oug+xrw -R /home/demiourgos1

COPY --chown=1001:1  entrypoint.sh /opt/workspace/entrypoint.sh
RUN chmod +x /opt/workspace/entrypoint.sh

ENTRYPOINT [ "/opt/workspace/entrypoint.sh" ]
