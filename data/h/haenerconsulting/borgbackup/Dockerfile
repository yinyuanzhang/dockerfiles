FROM alpine
ARG VERSION
ARG BUILD_DATE
ARG VCS_REF
ARG GIT_COMMIT=unspecified
LABEL org.label-schema.version=$VERSION
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url=https://github.com/haenerconsulting/borgbackup
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL git_commit=$GIT_COMMIT
LABEL maintainer="Patrick Haener <contact@haenerconsulting.com>"

RUN apk add --no-cache \
  borgbackup 

