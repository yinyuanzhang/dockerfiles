FROM khipu/base-alpine
MAINTAINER developers@khipu.com

ARG KHIPU_HOME=/opt/khipu
ENV KHIPU_HOME ${KHIPU_HOME}

ONBUILD ARG PROJECT_NAME
ONBUILD ARG PROJECT_VERSION
ONBUILD ENV PROJECT_NAME ${PROJECT_NAME}
ONBUILD ENV PROJECT_VERSION ${PROJECT_VERSION}

ONBUILD LABEL name=${PROJECT_NAME}
ONBUILD LABEL version=${PROJECT_VERSION}

RUN apk -U add openjdk8 npm \
    && rm -rf /var/cache/apk/*

RUN npm install -g diff2html@2.6.0 diff2html-cli@2.6.0

# jvm fixes
RUN sed -i 's/.*networkaddress.cache.ttl=.*/networkaddress.cache.ttl=5/g' /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security \
  && sed -i 's/.*networkaddress.cache.negative.ttl=.*/networkaddress.cache.negative.ttl=5/g' /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/java.security

COPY entrypoint.sh /

ONBUILD RUN mkdir -p ${KHIPU_HOME}/etc/${PROJECT_NAME} \
  && mkdir -p ${KHIPU_HOME}/log/${PROJECT_NAME}/ \
  && mkdir -p ${KHIPU_HOME}/share/${PROJECT_NAME}/ \
  && chown -R khipu:khipu ${KHIPU_HOME}/

ONBUILD COPY build/libs/${PROJECT_NAME}.war ${KHIPU_HOME}/share/${PROJECT_NAME}/

ONBUILD ENTRYPOINT ["/entrypoint.sh"]
