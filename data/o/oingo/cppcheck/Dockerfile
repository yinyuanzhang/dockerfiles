FROM alpine:3.8

ENV CPPCHECK_VERSION=1.87

RUN apk update && \
    apk add --no-cache -t .required_apks wget make g++ pcre-dev bash git openssh && \
    wget -q --no-check-certificate -O /tmp/cppcheck-${CPPCHECK_VERSION}.tar.gz https://github.com/danmar/cppcheck/archive/${CPPCHECK_VERSION}.tar.gz && \
    tar -zxf /tmp/cppcheck-${CPPCHECK_VERSION}.tar.gz -C /tmp && \
    cd /tmp/cppcheck-${CPPCHECK_VERSION} && \
    make install CFGDIR=/cfg HAVE_RULES=yes CXXFLAGS="-O2 -DNDEBUG -Wall -Wno-sign-compare -Wno-unused-function --static" && \
    apk del .required_apks && \
    rm -rf /tmp/cppcheck && \
    mkdir /src

CMD ["/bin/sh"]
