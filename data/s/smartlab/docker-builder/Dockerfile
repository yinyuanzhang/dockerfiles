#### BUILDER #############################################################
FROM ubuntu:18.04 

LABEL maintainer="smartlab-dev@mpt.mp.br"

ARG DEBIAN_FRONTEND="noninteractive"
ARG DEV="python3-pip libldap2-dev libsasl2-dev libffi-dev"

RUN apt-get update \
 && apt-get install -y $DEV
