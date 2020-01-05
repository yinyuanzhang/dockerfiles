# Copyright (c) 2018 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

FROM  clojure:openjdk-8-lein-2.9.1-alpine as build
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

ENV VERSION 30399b0a6f540d5d45970cc14b897814912a6f0c

RUN apk add git \
    && git clone https://github.com/qiuxiafei/zk-web.git \
    && cd zk-web \
    && git checkout ${VERSION} \
    && lein uberjar

FROM aristanetworks/openjdk:2.1
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"

COPY --from=build /tmp/zk-web/target/zk-web-0.2.0-standalone.jar /zk-web-0.2.0-standalone.jar

ENTRYPOINT ["/usr/bin/dumb-init", "--", "java", "-jar", "/zk-web-0.2.0-standalone.jar"]
