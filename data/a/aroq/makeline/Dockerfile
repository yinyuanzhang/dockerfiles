FROM google/cloud-sdk:218.0.0-alpine as google-cloud-sdk

FROM golang:1.10.4-alpine3.8
COPY rootfs/ /
RUN chown root:root /root/.ssh/config && chmod 600 /root/.ssh/config
WORKDIR /

# Install the cloudposse alpine repository
ADD https://apk.cloudposse.com/ops@cloudposse.com.rsa.pub /etc/apk/keys/
RUN echo "@cloudposse https://apk.cloudposse.com/3.8/vendor" >> /etc/apk/repositories

# Use TLS for alpine default repos
RUN sed -i 's|http://dl-cdn.alpinelinux.org|https://alpine.global.ssl.fastly.net|g' /etc/apk/repositories && \
    echo "@testing https://alpine.global.ssl.fastly.net/alpine/edge/testing" >> /etc/apk/repositories && \
    echo "@community https://alpine.global.ssl.fastly.net/alpine/edge/community" >> /etc/apk/repositories && \
    apk update

# Install alpine package manifest
COPY packages.txt /etc/apk/

RUN apk add --update $(grep -v '^#' /etc/apk/packages.txt)

ENV CLOUDSDK_CONFIG=/localhost/.config/gcloud/
COPY --from=google-cloud-sdk /google-cloud-sdk/ /usr/local/google-cloud-sdk/
RUN ln -s /usr/local/google-cloud-sdk/bin/gcloud /usr/local/bin/ && \
    ln -s /usr/local/google-cloud-sdk/bin/gsutil /usr/local/bin/ && \
    ln -s /usr/local/google-cloud-sdk/bin/bq /usr/local/bin/ && \
    gcloud config set core/disable_usage_reporting true --installation && \
    gcloud config set component_manager/disable_update_check true --installation && \
    gcloud config set metrics/environment github_docker_image --installation

COPY requirements.txt /requirements.txt
#RUN pip install -r /requirements.txt --install-option="--prefix=/dist" --no-build-isolation
RUN pip install -r /requirements.txt

# Volume for the secrets.
VOLUME ["/root/.config"]

ENV MAKELINE_PATH /makeline
ADD ./ ${MAKELINE_PATH}/
WORKDIR ${MAKELINE_PATH}

# TODO: Need to copy the binary from Uniconf docker image.
RUN go get github.com/aroq/uniconf

# Volume for the current context.
ENV UNIPIPE_PATH /unipipe
VOLUME [${UNIPIPE_PATH}]
WORKDIR ${UNIPIPE_PATH}

# Install variant
ENV VARIANT_VERSION 0.25.1
RUN curl --fail -sSL -o variant.tar.gz https://github.com/mumoshu/variant/releases/download/v${VARIANT_VERSION}/variant_${VARIANT_VERSION}_linux_386.tar.gz \
    && mkdir -p variant && \
    tar -zxf variant.tar.gz -C variant \
    && cp variant/variant /usr/local/bin/ \
    && rm -f variant.tar.gz \
    && rm -fR variant \
    && chmod +x /usr/local/bin/variant

# Install fd
ENV FD_VERSION 7.1.0
RUN curl --fail -sSL -o fd.tar.gz https://github.com/sharkdp/fd/releases/download/v${FD_VERSION}/fd-v${FD_VERSION}-x86_64-unknown-linux-musl.tar.gz \
    && tar -zxf fd.tar.gz \
    && cp fd-v${FD_VERSION}-x86_64-unknown-linux-musl/fd /usr/local/bin/ \
    && rm -f fd.tar.gz \
    && rm -fR fd-v${FD_VERSION}-x86_64-unknown-linux-musl \
    && chmod +x /usr/local/bin/fd
