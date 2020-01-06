FROM frolvlad/alpine-glibc:latest

MAINTAINER "Christopher Eagan" <ceagan@gmail.com>

# specify the version string of the oc release
ENV OC_VERSION "v3.6.0"
ENV OC_RELEASE "openshift-origin-client-tools-$OC_VERSION-c4dd4cf-linux-64bit"

# install the oc client tools
ADD https://github.com/openshift/origin/releases/download/$OC_VERSION/$OC_RELEASE.tar.gz /opt/oc/release.tar.gz
RUN apk add --no-cache ca-certificates
RUN tar --strip-components=1 -xzvf  /opt/oc/release.tar.gz -C /opt/oc/ && \
    mv /opt/oc/oc /usr/bin/ && \
    rm -rf /opt/oc

