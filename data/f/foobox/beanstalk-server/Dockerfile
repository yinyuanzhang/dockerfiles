ARG ARCH=amd64
ARG ALPINE_VERSION=3.8
FROM $ARCH/alpine:$ALPINE_VERSION

ARG BUILD_DATE
ARG VCS_URL
ARG VCS_REF
LABEL org.label-schema.schema-version=1.0
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url=$VCS_URL
LABEL maintainer="Andreas Treichel <gmblar+github@gmail.com>"

ARG BEANSTALKD_VERSION=1.10
EXPOSE 11300/tcp
ENV BEANSTALKD_BINLOG_INTERVAL=1000
COPY src /
RUN beanstalkd-setup
USER beanstalk
HEALTHCHECK CMD beanstalkd-healthcheck
ENTRYPOINT ["beanstalkd-entrypoint"]
CMD ["beanstalkd"]
