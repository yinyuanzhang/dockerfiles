# Extend the latest ubuntu image
FROM alpine:latest

# Set a working directory
WORKDIR /workspace/

# Update / Upgrade apk
RUN apk update

# Install apk packages
RUN apk add \
    nodejs \
    yarn \
    bash \
    curl \
    git \
    make \
    openssh-client \
    ca-certificates

# Install git-ftp
RUN git clone https://github.com/git-ftp/git-ftp.git /opt/git-ftp \
    && cd /opt/git-ftp \
    && tag="$(git tag | grep '^[0-9]*\.[0-9]*\.[0-9]*$' | tail -1)" \
    && git checkout "$tag" \
    && make install \
    && rm -rf /opt/git-ftp

# Set entrypoint as deploy.sh, we'll sort everything out in there
ENTRYPOINT ["sh", "deploy.sh"]
