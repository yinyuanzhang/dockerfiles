FROM katalonstudio/katalon

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="katalon" \
      org.label-schema.description="Katalon with curl" \
      org.label-schema.url="http://andradaprieto.es" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/jandradap/katalon" \
      org.label-schema.vendor="Jorge Andrada Prieto" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0" \
      maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \
      org.label-schema.docker.cmd=""

RUN apt-get update && \
    apt-get install --no-install-recommends -yq \
    curl \
    && apt-get clean

ENTRYPOINT [""]
