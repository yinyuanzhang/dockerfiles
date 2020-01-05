# GENERATED FILE -- DO NOT EDIT.
# See Dockerfile.zypper.tmpl
FROM opensuse:13.2
MAINTAINER qa@docker.com

CMD curl
RUN zypper --non-interactive update \
    && zypper --non-interactive install curl gnupg \
    && zypper clean
