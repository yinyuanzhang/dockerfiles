FROM openjdk:11.0.4-jre-slim

RUN apt-get update \
  && apt-get -y install gettext-base \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

VOLUME /tmp
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8
# Run as non-root
RUN groupadd -g 999 slotex && \
    useradd -r -u 999 -g slotex slotex
RUN mkdir -p /app && chown -R slotex:slotex /app
RUN mkdir /logs && chown -R slotex:slotex /logs
USER slotex
