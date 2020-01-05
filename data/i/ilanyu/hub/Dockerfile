FROM jetbrains/hub:2018.2.10527

MAINTAINER ilanyu <lanyu19950316@gmail.com>

COPY com.lanyus.crack.upsource.jar /opt/hub/lib/ext/com.lanyus.crack.upsource.jar

USER root

RUN sed -e '/#!\/bin\/bash/a export JAVA_TOOL_OPTIONS=-Xbootclasspath/p:/opt/hub/lib/ext/com.lanyus.crack.upsource.jar' -i /run.sh

USER 13001:13001

VOLUME /opt/hub/data /opt/hub/conf /opt/hub/logs /opt/hub/backups
