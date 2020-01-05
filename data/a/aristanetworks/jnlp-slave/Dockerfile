# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

FROM jenkins/jnlp-slave:3.27-1-alpine
LABEL maintainer="Giuseppe Valente gvalente@arista.com"

USER root

# Create the docker group with the same ID used in CoreOS
RUN addgroup -g 233 docker \
  && adduser jenkins docker \
  && apk add docker

USER jenkins
