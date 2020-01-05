#########################
# multi stage Dockerfile
# 1. build the website
# 2. run apache with php
#########################
FROM frekele/ant as builder
LABEL maintainer="Daniel Röwenstrunk for the ViFE"

RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN ant

# 2. Step

FROM stadlerpeter/existdb:latest
MAINTAINER Daniel Röwenstrunk <roewenstrunk@uni-paderborn.de>

ENV EDIROM_VERSION 0.9.1
ENV EDIROM_URL https://github.com/Edirom/Edirom-Online/releases/download/v${EDIROM_VERSION}/Edirom-Online-${EDIROM_VERSION}.xar

ENV EXIST_CONTEXT_PATH /
ENV EXIST_DEFAULT_APP_PATH xmldb:exist:///db/apps/EdiromOnline

COPY --from=builder /app/dist/*.xar /opt/exist/autodeploy/
ADD ${EDIROM_URL} /opt/exist/autodeploy/Edirom-Online-${EDIROM_VERSION}.xar

USER root
RUN chmod a+r /opt/exist/autodeploy/Edirom-Online-${EDIROM_VERSION}.xar
USER wegajetty