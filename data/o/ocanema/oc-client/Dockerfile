FROM frolvlad/alpine-glibc:latest

MAINTAINER "Mateus Menegon" <ocanema@gmail.com>

# specify the version string of the oc release
ENV OC_VERSION "v3.11.0"
ENV OC_RELEASE "openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit"
ENV RENDER_RELEASE "v0.0.8"


# install the oc client tools
ADD https://github.com/VirtusLab/render/releases/download/$RENDER_RELEASE/render-linux-amd64 /usr/bin/render
ADD https://github.com/openshift/origin/releases/download/$OC_VERSION/$OC_RELEASE.tar.gz /opt/oc/release.tar.gz
RUN apk add --no-cache ca-certificates && \
    tar --strip-components=1 -xzvf  /opt/oc/release.tar.gz -C /opt/oc/ && \
    mv /opt/oc/oc /usr/bin/ && \
    rm -rf /opt/oc && \
    chmod +x /usr/bin/render

EXPOSE 8001
