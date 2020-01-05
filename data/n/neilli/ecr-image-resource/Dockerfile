FROM alpine

ARG pip_installer="https://bootstrap.pypa.io/get-pip.py"

# Install dependent packages
RUN apk --update add \
    bash \
    jq \
    ca-certificates \
    docker \
    python \
    curl \
    groff

# Install awscli
RUN curl ${pip_installer} | python && \
    pip install awscli

COPY check.sh /opt/resource/check
COPY in.sh /opt/resource/in
COPY out.sh /opt/resource/out

RUN chmod +x /opt/resource/check /opt/resource/in /opt/resource/out
