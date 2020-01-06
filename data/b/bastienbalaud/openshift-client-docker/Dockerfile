FROM debian:stable-slim

ENV OC_VERSION "v3.11.0"
ENV OC_RELEASE "openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit"
RUN apt-get update && apt-get install wget -y && apt clean all
RUN wget https://github.com/openshift/origin/releases/download/$OC_VERSION/$OC_RELEASE.tar.gz -O /tmp/release.tar.gz && tar --strip-components=1 -xvzf /tmp/release.tar.gz -C /bin/ $OC_RELEASE/oc && rm -rf /tmp/release.tar.gz
